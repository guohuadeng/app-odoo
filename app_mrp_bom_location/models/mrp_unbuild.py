# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class MrpUnbuild(models.Model):
    _inherit = "mrp.unbuild"

    @api.onchange('bom_id')
    def onchange_bom_id(self):
        if self.bom_id.location_id:
            self.location_id = self.bom_id.location_id
            self.location_dest_id = self.bom_id.location_id

