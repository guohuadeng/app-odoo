# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Department(models.Model):
    # 目录图片，可显示小图标，
    _name = "hr.department"
    _inherit = ['hr.department', 'image.mixin']

    # 目录图片，可显示小图标，odoo13 在 mixin 中处理了


    child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_child_all_count', store=False)

    manager_name = fields.Char(related="manager_id.name", store=True)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)
