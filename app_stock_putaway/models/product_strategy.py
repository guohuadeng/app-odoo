# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class PutAwayStrategy(models.Model):
    _inherit = 'product.putaway'

    # 增加默认父位置
    location_id = fields.Many2one('stock.location', 'Location')

    @api.model
    def create(self, vals):
        location_id = self.env.context.get('location_id')
        vals['location_id'] = location_id
        return super(PutAwayStrategy, self).create(vals)


