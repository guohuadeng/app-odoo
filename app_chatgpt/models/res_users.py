# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    # 改为在 partner中设置，用户处绑定
    gpt_id = fields.Many2one('ai.robot', string='Bind to Ai', related='partner_id.gpt_id', inherited=True, readonly=False)
    gpt_policy = fields.Selection([
        ('all', 'All Users'),
        ('limit', 'Selected Users')
    ], string='Allowed Conversation Mode', default='all', ondelete='set default')
    gpt_wl_partners = fields.Many2many('res.partner', 'res_partner_ai_use', 'ai_user_id', 'name', string='Allowed Partners')
    gpt_demo_time = fields.Integer('Default Demo Time', default=0)
    is_chat_private = fields.Boolean('Allow Chat Private', default=False, related='partner_id.is_chat_private', inherited=True, readonly=False)