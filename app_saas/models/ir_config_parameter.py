# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import models

_logger = logging.getLogger(__name__)

DB_TOKEN_KEY = 'app_saas_db_token'


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self, force=False):
        super(IrConfigParameter, self).init(force=force)
        if not force:
            return
        # force=True 只会出现在两种情况：全新库初始化（base.post_init）和数据库被
        # 复制/克隆（Odoo 的 duplicate、restore as copy，见 odoo/service/db.py）。
        # 后者的 base.init(force=True) 已经重新生成了 database.uuid，而原库的
        # 实例令牌（app_saas_db_token，与 oauth provider 的 client_secret 同一值）
        # 仍指向旧库身份，必须清空，否则克隆库会拿着旧令牌冒用原库与云端通信；
        # 新库首次连接云端时会重新下发令牌并写回。
        self._app_saas_reset_cloned_params()

        oauth_app_saas = self.env.ref('app_saas.provider_app_saas', raise_if_not_found=False)
        if not oauth_app_saas:
            return
        # client_id 跟随新库的 database.uuid，与云端 oauth2.client 的对接键保持一致
        dbuuid = self.sudo().get_param('database.uuid')
        oauth_app_saas.write({'client_id': dbuuid})

    def _app_saas_reset_cloned_params(self):
        """克隆/初始化数据库时，清空继承自原库的实例级凭据与身份。

        - app_saas_db_token：实例令牌（与 oauth provider 的 client_secret 同一值）

        都按“有值才清”处理，避免在新库上留下空参数行或多余写库。
        注：18 版 app_saas 无云通道（cloud_tunnel_*）设置，也无 app_saas_tunnel
        模块，故只清实例令牌；隧道相关 key 的重置仅在 20 版。
        """
        cleared = []

        ictoken = self.sudo().get_param(DB_TOKEN_KEY)
        if ictoken:
            # o18 的 set_param(key, False) 会直接 unlink 该参数行，不留空值
            self.sudo().set_param(DB_TOKEN_KEY, False)
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

        if cleared:
            _logger.info(
                "app_saas: database was cloned/initialized, cleared instance params %s "
                "(database.uuid=%s)", cleared, self.sudo().get_param('database.uuid'),
            )