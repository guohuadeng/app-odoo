# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


# Record the net weight of the order line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # 显示的单位，影响性能暂时不使用
    # weight_uom_name = fields.Char(string='Weight Measure', related='product_id.weight_uom_id.name', readonly=True)
    # 调整，根据 delivery 模块，将 weight 作为 该行合计，weight_unit 作为该单位的
    weight_unit = fields.Float(string='Weight Unit', compute='_compute_weight', store=True)
    weight = fields.Float(string='Weight Subtotal', compute='_compute_weight', store=True)

    @api.multi
    @api.depends('product_id', 'product_uom', 'product_uom_qty')
    def _compute_weight(self):
        for line in self.filtered(lambda rec: rec.product_id.weight > 0.00):
            weight = 0
            try:
                weight_unit = line.product_id.weight / line.product_uom.factor
            except:
                weight_unit = line.product_id.weight
            weight += (weight_unit * line.product_uom_qty)
            line.weight_unit = weight_unit
            line.weight = weight

    @api.one
    def _set_weight_subtotal(self):
        pass
