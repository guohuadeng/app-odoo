# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


# Record the net weight of the order line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    weight = fields.Float(string='Weight', store=True)
    weight_subtotal = fields.Float(string='Weight Subtotal', compute='_compute_weight_subtotal',
                          inverse='_set_weight_subtotal', store=True)

    @api.multi
    @api.depends('product_id', 'product_uom_qty')
    def _compute_weight_subtotal(self):
        for line in self:
            weight = 0
            if line.product_id and line.product_id.weight:
                weight += (line.product_id.weight * line.product_uom_qty / line.product_uom.factor)
            line.weight = weight

    @api.one
    def _set_weight_subtotal(self):
        pass
