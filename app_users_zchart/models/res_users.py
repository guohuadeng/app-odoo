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

