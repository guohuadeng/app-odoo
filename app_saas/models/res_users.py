# -*- coding: utf-8 -*-

try:
    import urlparse
except:
    from urllib.parse import urlparse
try:
    import urllib2
except:
    from urllib import request as urllib2

from odoo import api, fields, models, _
import requests

import logging

_logger = logging.getLogger(__name__)


class OauthBindError(Exception):
    # 增加一种错误类型
    pass


class ResUsers(models.Model):
    _inherit = 'res.users'
    
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
    
    def _auth_oauth_signin(self, provider, validation, params):
        # 用户绑定的额外处理，如果有同 login 用户则直接绑定
        # todo: 当前不管多公司，在 social_login 里有更细节判断，后续优化
        # todo: 当前同名就写 oauth 信息，不安全，要优化
        oauth_provider = self.env['auth.oauth.provider'].sudo().browse(provider)
        if oauth_provider and oauth_provider.scope.find('odoo') >= 0:
            oauth_uid = validation.get('user_id')
            if oauth_uid:
                odoo_user = self.sudo().search([('login', '=', oauth_uid)], limit=1)
                if odoo_user and not (odoo_user.oauth_access_token and odoo_user.oauth_provider_id and odoo_user.oauth_uid):
                    vals = {
                        'oauth_provider_id': provider,
                        'oauth_access_token': params.get('access_token'),
                        'oauth_uid': oauth_uid,
                    }
                    odoo_user.write(vals)
                    _logger.info('========= _auth_oauth_signin res.users write：%s' % vals)
                    self._cr.commit()
                    return odoo_user.user_id.login
        res = super(ResUsers, self)._auth_oauth_signin(provider, validation, params)
        return res
        
    @api.model
    def _generate_signup_values(self, provider, validation, params):
        # 此处生成 创建 odoo user 的初始值，增加字段如头像
        res = super()._generate_signup_values(provider, validation, params)
        # 后置增加字段，包括 headimgurl
        if validation.get('mobile'):
            res['mobile'] = validation.get('mobile')
        if validation.get('headimgurl'):
            res['image_1920'] = self.sudo()._get_image_from_url(validation.get('headimgurl'))
        return res
    
    def _rpc_api_keys_only(self):
        # 当 not 时可直接使用 oauth_access_token 作为 password 登录
        self.ensure_one()
        return not self.oauth_access_token or super()._rpc_api_keys_only()
