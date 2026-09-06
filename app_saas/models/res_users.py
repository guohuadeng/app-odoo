# -*- coding: utf-8 -*-

try:
    import urlparse
except:
    from urllib.parse import urlparse
try:
    import urllib2
except:
    from urllib import request as urllib2

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.base.models.res_users import KEY_CRYPT_CONTEXT, INDEX_SIZE
from odoo.addons.auth_signup.models.res_users import SignupError

from ast import literal_eval
import requests

import logging

_logger = logging.getLogger(__name__)


class OauthBindError(Exception):
    # 增加一种错误类型
    pass


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _create_user_from_template(self, values):
        # 处理可指定 user template
        oauth_provider_id = values.get('oauth_provider_id', 0)
        if oauth_provider_id:
            provider = self.env['auth.oauth.provider'].sudo().browse(int(oauth_provider_id))
            if provider and provider.user_template_id:
                template_user_id = literal_eval(str(provider.user_template_id.id))
                template_user = self.browse(template_user_id)
                if not template_user.exists():
                    raise ValueError(_('Signup: invalid template user'))

                if not values.get('login'):
                    raise ValueError(_('Signup: no login given for new user'))
                if not values.get('partner_id') and not values.get('name'):
                    raise ValueError(_('Signup: no name or partner given for new user'))

                # create a copy of the template user (attached to a specific partner_id if given)
                values['active'] = True
                try:
                    with self.env.cr.savepoint():
                        return template_user.with_context(no_reset_password=True).copy(values)
                except Exception as e:
                    # copy may failed if asked login is not available.
                    raise SignupError(str(e))
        res = super(ResUsers, self)._create_user_from_template(values)
        self._cr.commit()
        return res
    
    @api.model
    def get_token_from_code(self, provider, params):
        # 通过 code 取 token
        # 这里原生是没处理code模式，此处将增加使用code取token，不在 controller 中处理
        oauth_provider = self.env['auth.oauth.provider'].sudo().browse(provider)

        # odoo 特殊处理，用code取token
        params.update({
            'scope': oauth_provider.scope or '',
            'client_id': oauth_provider.client_id or '',
        })
        if hasattr(oauth_provider, 'client_secret') and oauth_provider.client_secret:
            params.update({
                'client_secret': oauth_provider.client_secret or '',
            })
        response = requests.get(oauth_provider.code_endpoint, params=params, timeout=30)
        if response.ok:
            ret = response.json()
            # 客户机首次连接时，取到的 server 端 key 写入 provider 的 client_secret
            push_client_secret = ret.pop('push_client_secret', False)
            if push_client_secret:
                ICP = self.env['ir.config_parameter'].sudo()
                ICP.set_param('app_saas_db_token', push_client_secret)
                if hasattr(oauth_provider, 'client_secret'):
                    oauth_provider.write({'client_secret': push_client_secret})
                self._cr.commit()
            return ret
        return {}

    @api.model
    def auth_oauth(self, provider, params):
        code = params.get('code', False)
        access_token = params.get('access_token')
        oauth_provider = self.env['auth.oauth.provider'].sudo().browse(provider)
        # 额外code 处理
        kw = params
        if oauth_provider.code_endpoint and code and not access_token:
            ret = self.sudo().get_token_from_code(provider, params)
            kw.update(ret)
            kw.pop('code', False)

        self = self.with_context(auth_extra=kw)
        res = super(ResUsers, self).auth_oauth(provider, kw)
        return res

    def _oauth_ensure_mcp_key(self, odoo_user, validation, access_token):
        """OAuth 登录时同步创建用户 MCP Key（对接 Work Buddy、Claude Code 等智能体）。
        仅当 passport 下发 is_create_mcp 且该用户尚无 scope 含 mcp 的有效 key 时创建。"""
        if not odoo_user or not validation.get('is_create_mcp', False):
            return
        # 已有 scope 含 mcp 的有效 key（未过期或永久）则不重复创建
        now = fields.datetime.now()
        for k in odoo_user.api_key_ids:
            if 'mcp' in (k.scope or '') and (not k.expiration_date or k.expiration_date > now):
                _logger.info('===== _oauth_ensure_mcp_key skip: user %s has valid mcp key #%s'
                             % (odoo_user.login, k.id))
                return
        mcp_expiration_date = validation.get('mcp_expiration_date', fields.datetime.now())
        mcp_scope = validation.get('mcp_scope', 'mcp,profile')
        mcp_name = validation.get('mcp_name', 'MCP odooapp')
        # 参考 core res.users.apikeys._generate 直接 SQL 插入：
        # _generate 取 env.user.id，登录流程中 with_user 不能保证 user_id 正确，
        # 此处显式写入 odoo_user.id；key 直接用 oauth access_token（与 app_mcp
        # fix_user_key 语义一致，智能体用同一 token 访问 MCP）
        key = access_token
        self.env.cr.execute("""
            INSERT INTO res_users_apikeys (name, user_id, scope, expiration_date, key, index)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """, [mcp_name, odoo_user.id, mcp_scope, mcp_expiration_date or None,
              KEY_CRYPT_CONTEXT.hash(key), key[:INDEX_SIZE]])
        key_id = self.env.cr.fetchone()[0]
        _logger.info('===== _oauth_ensure_mcp_key created #%s for user %s'
                     % (key_id, odoo_user.login))
        # app_mcp 安装时（user_key 列存在）同步明文 key，供 MCP 配置生成使用
        # self.env.cr.execute("""
        #     SELECT EXISTS (
        #         SELECT 1 FROM pg_attribute
        #         WHERE attname = 'user_key'
        #         AND attrelid = (SELECT oid FROM pg_class WHERE relname = 'res_users_apikeys')
        #     );
        # """)
        # if self.env.cr.fetchone()[0]:
        #     self.env.cr.execute(
        #         "UPDATE res_users_apikeys SET user_key = %s WHERE id = %s", [key, key_id])

    def _auth_oauth_signin(self, provider, validation, params):
        # 用户绑定的额外处理，如果有同 login 用户则直接绑定
        # todo: 当前不管多公司，在 social_login 里有更细节判断，后续优化
        # todo: 当前同名就写 oauth 信息，不安全，要优化
        oauth_provider = self.env['auth.oauth.provider'].sudo().browse(provider)
        access_token = params.get('access_token')
        if oauth_provider and ('odoo' in (oauth_provider.scope or '') or 'client' in (oauth_provider.scope or '')):
            oauth_uid = validation.get('user_id')
            if oauth_uid:
                odoo_user = self.sudo().search([('login', '=', oauth_uid)], limit=1)
                if odoo_user and not (odoo_user.oauth_access_token and odoo_user.oauth_provider_id and odoo_user.oauth_uid):
                    vals = {
                        'oauth_provider_id': provider,
                        'oauth_access_token': access_token,
                        'oauth_uid': oauth_uid,
                    }
                    odoo_user.write(vals)
                    _logger.info('========= _auth_oauth_signin res.users write：%s' % vals)
                    # 增加处理写mcp key
                    self._oauth_ensure_mcp_key(odoo_user, validation, access_token)
                    self._cr.commit()
                    return odoo_user.login
        res = super(ResUsers, self)._auth_oauth_signin(provider, validation, params)
        # 增加处理写mcp key（用户已绑定过 oauth 走此分支；
        # 按 validation.user_id 找回用户，避免原代码此处 odoo_user 未定义）
        odoo_user = self.sudo().search([('login', '=', validation.get('user_id'))], limit=1)
        self._oauth_ensure_mcp_key(odoo_user, validation, access_token)
        return res

    @api.model
    def _generate_signup_values(self, provider, validation, params):
        # 此处生成 创建 odoo user 的初始值，增加字段如头像
        res = super()._generate_signup_values(provider, validation, params)
        # 后置增加字段，包括 headimgurl
        if validation.get('mobile'):
            res['mobile'] = validation.get('mobile')
        if validation.get('headimgurl'):
            res['image_1920'] = self.with_user(SUPERUSER_ID)._get_image_from_url(validation.get('headimgurl'))
        return res

    # def _rpc_api_keys_only(self):
    #     # 当 false 时可直接使用 oauth_access_token 作为 password 登录
    #     self.ensure_one()
    #     return not self.oauth_access_token or super()._rpc_api_keys_only()

    def clean_user_oauth_token_window(self):
        self.write({
            'oauth_access_token': False,
            'oauth_provider_id': False,
            'oauth_uid': False,
        })
        return {
            'effect': {
                'type': 'rainbow_man',
                'message': _("Successfully clear the token of [%s] oauth users. " % len(self)),
            }
        }
