# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import models

_logger = logging.getLogger(__name__)

DB_TOKEN_KEY = 'app_saas_db_token'
TUNNEL_KEY = 'app_saas.cloud_tunnel_key'
# agent 回报的陈旧状态展示：克隆库会继承原库的在线假象，一并清空，
# 待新库自己的 agent 首次回报后重新写入。
TUNNEL_STATUS_KEYS = (
    'app_saas.cloud_tunnel_status',
    'app_saas.cloud_tunnel_last_seen',
    'app_saas.cloud_tunnel_last_error',
)


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self, force=False):
        super(IrConfigParameter, self).init(force=force)
        if not force:
            return
        # force=True 只会出现在两种情况：全新库初始化（base.post_init）和数据库被
        # 复制/克隆（Odoo 的 duplicate、restore as copy，见 odoo/modules/db.py）。
        # 后者的 base.init(force=True) 已经重新生成了 database.uuid，而原库的
        # 实例令牌（app_saas_db_token，与 oauth provider 的 client_secret 同一值）
        # 仍指向旧库身份，必须清空，否则克隆库会拿着旧令牌冒用原库与云端通信；
        # 新库首次连接云端时会重新下发令牌并写回。
        self._app_saas_reset_cloned_params()

        oauth_app_saas = self.env.ref('app_saas.provider_app_saas', raise_if_not_found=False)
        if not oauth_app_saas:
            return
        # client_id 跟随新库的 database.uuid，与云端 oauth2.client 的对接键保持一致
        dbuuid = self.sudo().get_str('database.uuid')
        oauth_app_saas.write({'client_id': dbuuid})

    def _app_saas_reset_cloned_params(self):
        """克隆/初始化数据库时，清空继承自原库的实例级凭据与身份。

        - app_saas_db_token：实例令牌（与 oauth provider 的 client_secret 同一值）
        - app_saas.cloud_tunnel_key：隧道路由键，清空后回退到新库的 database.uuid
        - app_saas.cloud_tunnel_status/last_seen/last_error：agent 回报的陈旧状态展示

        都按“有值才清”处理，避免在新库上留下空参数行或多余写库。
        """
        cleared = []

        ictoken = self.sudo().get_str(DB_TOKEN_KEY)
        if ictoken:
            self.sudo().set_str(DB_TOKEN_KEY, False)
            cleared.append(DB_TOKEN_KEY)

        provider = self.env.ref('app_saas.provider_app_saas', raise_if_not_found=False)
        provider_token = (
            provider
            and 'client_secret' in provider._fields
            and provider.client_secret
        )
        if provider_token:
            provider.write({'client_secret': False})
            cleared.append('auth.oauth.provider.client_secret')

        tunnel_key = self.sudo().get_str(TUNNEL_KEY)
        if tunnel_key:
            self.sudo().set_str(TUNNEL_KEY, False)
            cleared.append(TUNNEL_KEY)

        for key in TUNNEL_STATUS_KEYS:
            if self.sudo().get_str(key):
                self.sudo().set_str(key, False)
                cleared.append(key)

        if cleared:
            _logger.info(
                "app_saas: database was cloned/initialized, cleared instance params %s "
                "(database.uuid=%s)", cleared, self.sudo().get_str('database.uuid'),
            )
