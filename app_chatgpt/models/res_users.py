# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd.(广州欧度智能科技有限公司) https://www.odooai.cn
#    Author: Ivan Deng，ivan@odooai.cn   300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.

#    Create on 2024-10-06
##############################################################################

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
