# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Users(models.Model):
    _inherit = "res.users"

    # 注意，res.partner 有 parent_id 和 child_ids
    _parent_name = "user_parent_id"
    _parent_store = True
    parent_path = fields.Char(index=True)

    user_parent_id = fields.Many2one('res.users', string='Parent User', index=True)
    user_child_ids = fields.One2many('res.users', 'user_parent_id', string='Sub Users', domain=[('active', '=', True)])

    user_child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_user_child_all_count', store=False)


    @api.depends('user_child_ids.user_child_all_count')
    def _compute_user_child_all_count(self):
        for rec in self:
            rec.user_child_all_count = len(rec.user_child_ids) + sum(child.user_child_all_count for child in rec.user_child_ids)
