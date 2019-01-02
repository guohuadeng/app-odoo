# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


# Record the net weight of the order line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # 显示的单位，影响性能暂时不使用
    # weight_uom_name = fields.Char(string='Weight Measure', related='product_id.weight_uom_id.name', readonly=True)
    weight = fields.Float(string='Weight', compute='_compute_weight', store=True)
    weight_subtotal = fields.Float(string='Weight Subtotal', compute='_compute_weight', store=True)

    @api.multi
    @api.depends('product_id', 'product_uom', 'product_qty')
    def _compute_weight(self):
        for line in self:
            weight = 0
            weight_subtotal = 0
            if line.product_id and line.product_id.weight:
                weight = line.product_id.weight / line.product_uom.factor
                weight_subtotal += (weight * line.product_qty)
            line.weight = weight
            line.weight_subtotal = weight_subtotal

    @api.one
    def _set_weight_subtotal(self):
        pass
