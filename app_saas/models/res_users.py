# -*- coding: utf-8 -*-

from odoo import api, fields, models, release, SUPERUSER_ID, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.tools.misc import ustr

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
        # 处理可指定 user template（与 v18 一致），并保留 v13 的 SaaS 内部用户模板回退
        oauth_provider_id = values.get('oauth_provider_id', 0)
        if oauth_provider_id:
            provider = self.env['auth.oauth.provider'].sudo().browse(int(oauth_provider_id))
            if provider:
                template_user = provider.user_template_id.sudo()
                if not template_user:
                    # v13 专有逻辑：Ai 通行证（odoo / client 范围）默认按内部用户创建，
                    # 其余情况沿用 base 参数指定的门户用户模板
                    if 'odoo' in (provider.scope or '') or 'client' in (provider.scope or ''):
                        template_user = self.sudo().env.ref('base.default_user', False)
                    if not template_user:
                        template_user_id = literal_eval(
                            self.env['ir.config_parameter'].sudo().get_param(
                                'base.template_portal_user_id', 'False'))
                        template_user = self.sudo().browse(template_user_id)

                if not values.get('login'):
                    raise ValueError(_('Signup: no login given for new user'))
                if not values.get('partner_id') and not values.get('name'):
                    raise ValueError(_('Signup: no name or partner given for new user'))

                # create a copy of the template user (attached to a specific partner_id if given)
                values['active'] = True
                try:
                    with self.env.cr.savepoint():
                        return template_user.sudo().with_context(no_reset_password=True).copy(values)
                except Exception as e:
                    # copy may failed if asked login is not available.
                    raise SignupError(ustr(e))
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
        # 向 Ai 通行证（data 里的 provider）上报本实例的详细 Odoo 版本号 v（如 13.0+e-20250101），
        # 通行证端据此回填 oauth2.client 的 version / full_version
        provider_app_saas = self.env.ref('app_saas.provider_app_saas')
        if oauth_provider.id == provider_app_saas.id:
            params.update({'v': release.version})
        response = requests.get(oauth_provider.code_endpoint, params=params, timeout=30)
        if response.ok:
            ret = response.json()
            # 客户机首次连接时，取到的 server 端 key 写入 ICP（app_saas_db_token）与 provider 的 client_secret
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
                    # 同步通行证头像到本库用户
                    self._oauth_sync_avatar(odoo_user, validation)
                    self._cr.commit()
                    return odoo_user.login
        res = super(ResUsers, self)._auth_oauth_signin(provider, validation, params)
        # 用户已绑定过 oauth 走此分支，按 validation.user_id 找回用户同步头像
        odoo_user = self.sudo().search([('login', '=', validation.get('user_id'))], limit=1)
        self._oauth_sync_avatar(odoo_user, validation)
        return res

    def _oauth_sync_avatar(self, odoo_user, validation):
        # OAuth 登录时同步通行证头像到本库用户。
        # headimg_data：passport 下发的 data:image/...;base64 头像数据，直接写值；
        # headimgurl：仍按 url 处理（远程取图）。
        # 值与当前头像一致时跳过写入，避免每次登录重复写库
        if not odoo_user:
            return
        headimg_data = validation.get('headimg_data')
        headimgurl = validation.get('headimgurl')
        image = False
        if headimg_data and headimg_data.startswith('data:'):
            image = headimg_data.split(',', 1)[-1]
        elif headimgurl and headimgurl.startswith('http'):
            image = self.with_user(SUPERUSER_ID)._get_image_from_url(headimgurl)
        if not image:
            return
        try:
            current = odoo_user.sudo().image_1920
            new_val = image if isinstance(image, bytes) else image.encode()
            if current != new_val:
                odoo_user.sudo().write({'image_1920': image})
        except Exception as e:
            _logger.warning('===== _oauth_sync_avatar error: %s' % str(e))

    @api.model
    def _generate_signup_values(self, provider, validation, params):
        # 此处生成 创建 odoo user 的初始值，增加字段如头像
        res = super(ResUsers, self)._generate_signup_values(provider, validation, params)
        # 后置增加字段：headimg_data 直接写值，headimgurl 按 url 取图
        if validation.get('mobile'):
            res['mobile'] = validation.get('mobile')
        headimg_data = validation.get('headimg_data')
        if headimg_data and headimg_data.startswith('data:'):
            res['image_1920'] = headimg_data.split(',', 1)[-1]
        elif validation.get('headimgurl'):
            res['image_1920'] = self.with_user(SUPERUSER_ID)._get_image_from_url(
                validation.get('headimgurl'))
        return res

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
