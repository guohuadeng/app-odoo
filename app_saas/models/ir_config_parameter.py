# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def init(self, force=False):
        super(IrConfigParameter, self).init(force=force)
        if force:
            oauth_app_saas = self.env.ref('app_saas.provider_app_saas')
            if not oauth_app_saas:
                return
            dbuuid = self.sudo().get_param('database.uuid')
            oauth_app_saas.write({'client_id': dbuuid})
