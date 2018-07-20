# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _

# Record the net weight of the order line
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    weight = fields.Float(string='Weight(kg)', compute='_compute_weight',
                              inverse='_set_weight', store=True)

    def _compute_weight(self):
        for line in self:
            weight = 0
            if line.product_id and line.product_id.weight:
                weight += (line.product_id.weight
                        * line.product_uom_qty / line.product_uom.factor)
            line.weight = weight

    @api.one
    def _set_weight(self):
        pass
