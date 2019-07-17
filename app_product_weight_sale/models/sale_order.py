# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_default_weight_uom_name(self):
        # todo: 此处没有处理翻译，后续调整
        get_param = self.env['ir.config_parameter'].sudo().get_param
        product_weight_in_lbs_param = get_param('product.weight_in_lbs')
        if product_weight_in_lbs_param == '1':
            return self.env.ref('uom.product_uom_lb').name
        else:
            return self.env.ref('uom.product_uom_kgm').name

    weight = fields.Float(string='Total Weight', compute='_compute_weight')
    # 重量显示的单位
    weight_uom_name = fields.Char(string='Weight Measure', default=_get_default_weight_uom_name, readonly=True)

    @api.multi
    @api.depends('order_line.weight')
    def _compute_weight(self):
        for rec in self:
            weight_tot = 0
            for line in rec.order_line:
                if line.product_id:
                    weight_tot += line.weight or 0.0
            rec.weight = weight_tot

