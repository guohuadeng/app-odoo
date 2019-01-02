# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_default_weight_uom_name(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        product_weight_in_lbs_param = get_param('product.weight_in_lbs')
        if product_weight_in_lbs_param == '1':
            return self.env.ref('uom.product_uom_lb').name
        else:
            return self.env.ref('uom.product_uom_kgm').name

    weight_total = fields.Float(string='Total Weight', compute='_compute_weight_total', store=True)
    # 重量显示的单位
    weight_uom_name = fields.Char(string='Weight Measure', default=_get_default_weight_uom_name, readonly=True)

    def _compute_weight_total(self):
        for rec in self:
            weight_tot = 0
            for line in rec.order_line:
                if line.product_id:
                    weight_tot += line.weight_subtotal or 0.0
            rec.weight_total = weight_tot

