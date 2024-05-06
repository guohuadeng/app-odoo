# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # 当前不处理到 sku
    product_brand_id = fields.Many2one(
        'product.brand',
        string='Brand',
        help='Select a brand for this product'
    )
