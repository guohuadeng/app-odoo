# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"

    # 注意，res.partner 有 parent_id 和 child_ids
    _parent_name = "parent_id"
    # _parent_store = True
    # parent_path = fields.Char(index=True)
    #
    # child_all_count = fields.Integer(
    #     'Indirect Surbordinates Count',
    #     compute='_compute_child_all_count', store=True)
    #
    #
    # @api.depends('child_ids.child_all_count')
    # def _compute_child_all_count(self):
    #     for rec in self:
    #         try:
    #             c_count = sum(child.child_all_count for child in rec.child_ids)
    #             rec.child_all_count = len(rec.child_ids) + c_count
    #         except Exception as e:
    #             rec.child_all_count = 0
