# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self, force=False):
        super(IrConfigParameter, self).init(force=force)
        if force:
            # force=True 会在 base 安装完成、数据库复制/恢复时触发，此时本模块可能尚未安装，
            # 故不能直接 ref 抛错（否则无 app_saas 的库会初始化失败）
            oauth_app_saas = self.env.ref('app_saas.provider_app_saas', raise_if_not_found=False)
            if not oauth_app_saas:
                return
            dbuuid = self.sudo().get_param('database.uuid')
            oauth_app_saas.write({'client_id': dbuuid})
