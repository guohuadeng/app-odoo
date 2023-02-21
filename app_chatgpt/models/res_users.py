# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    gpt_id = fields.Many2one('gpt.robot', string='Bind to ChatGpt')
    gpt_policy = fields.Selection([
        ('all', 'All Users'),
        ('limit', 'Selected Users')
    ], string='Allowed Conversation Mode', default='all', ondelete='set default')
    gpt_wl_users = fields.Many2many('res.users', 'res_users_res_users_rel', 'robot_id', 'user_id', string='Allowed Users', domain="[('id', '!=', id)]")
    gpt_demo_time = fields.Integer('Default Demo Time', default=0)
