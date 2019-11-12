# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = ['product.category', 'image.mixin']

    # 目录图片，可显示小图标，odoo13 在 mixin 中处理了

    child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_child_all_count', store=False)

    @api.depends('child_id.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_id) + sum(child.child_all_count for child in rec.child_id)
