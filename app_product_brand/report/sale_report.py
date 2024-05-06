# -*- coding: utf-8 -*-

from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_brand_id = fields.Many2one('product.brand', string='Product Brand', readonly=True)
    
    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['product_brand_id'] = "l.product_brand_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res = res + ",l.product_brand_id"
        return res
