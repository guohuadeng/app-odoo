# -*- coding: utf-8 -*-
import logging
from odoo import fields, models, api, _

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_brand_id = fields.Many2one(
        'product.brand',
        string='Brand',
        compute='_compute_product_code',
        readonly=True, store=True,
        help='Select a brand for this product'
    )

    @api.depends('product_id')
    def _compute_product_code(self):
        # 直接覆盖 app_sale_pro
        data = self.env['product.product'].search_read([('id', 'in', self.mapped('product_id').ids)],
                                                       fields=['id', 'default_code', 'product_brand_id'])
        for rec in self:
            rec.product_code = rec.product_id.default_code
            rec.categ_id = rec.product_id.categ_id
            rec.product_brand_id = rec.product_id.product_brand_id
            
        # for rec in self:
        #     rec.update({
        #         'product_code': data[rec.product_id.id].get('default_code'),
        #         'product_brand_id':  data[rec.product_id.id].get('product_brand_id')
        #     })

            