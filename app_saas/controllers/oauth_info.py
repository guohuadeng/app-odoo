# -*- coding: utf-8 -*-
"""OdooApp 移动端 OAuth 入口。

客户端 Odoo 安装 app_saas 后，APK 通过该只读接口拿到与网页
“Ai Passport of odooapp.cn” 按钮等价的授权地址，再走标准
OAuth2 授权码流程。接口不返回 client_secret、不创建会话、不改数据。
"""

import json

import werkzeug.urls
from odoo import http
from odoo.http import request


class AppSaasOAuthInfo(http.Controller):

    def _disabled(self, reason, provider=None):
        return {
            'enabled': False,
            'reason': reason,
            'provider_name': provider.name if provider else '',
        }

    @http.route('/app_saas/oauth_info', type='json', auth='public', csrf=False)
    def oauth_info(self, **kwargs):
        provider = request.env.ref('app_saas.provider_app_saas', raise_if_not_found=False)
        provider = provider.sudo() if provider else provider
        if not provider:
            return self._disabled('provider_missing')
        if not provider.enabled:
            return self._disabled('provider_disabled', provider)
        if not provider.auth_endpoint:
            return self._disabled('auth_endpoint_missing', provider)
        if not provider.client_id:
            return self._disabled('client_id_missing', provider)

        # 与 Odoo 网页 OAuth 按钮一致：回调到本实例 /auth_oauth/signin，
        # state 里带 db / provider / 登录后目标地址，客户端 auth_oauth 依赖它。
        base = request.httprequest.url_root.rstrip('/')
        redirect_uri = base + '/auth_oauth/signin'
        redirect_target = werkzeug.urls.url_quote_plus(base + '/web')
        dbname = request.db or request.session.db
        state = json.dumps({
            'd': dbname,
            'p': provider.id,
            'r': redirect_target,
        })
        # app_saas 的 Ai 通行证使用 code_endpoint（code 换 token）；
        # 其他标准 provider 仍按 Odoo 默认的 token 模式拼链接。
        response_type = 'code' if provider.code_endpoint else 'token'
        scope = provider.scope or 'client,profile'
        params = {
            'response_type': response_type,
            'client_id': provider.client_id,
            'redirect_uri': redirect_uri,
            'scope': scope,
            'state': state,
        }
        auth_url = '%s?%s' % (provider.auth_endpoint, werkzeug.urls.url_encode(params))

        return {
            'enabled': True,
            'provider_id': provider.id,
            'provider_name': provider.name,
            'client_id': provider.client_id,
            'redirect_uri': redirect_uri,
            'scope': scope,
            'state': state,
            'response_type': response_type,
            'auth_url': auth_url,
        }
