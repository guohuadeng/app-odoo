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
from odoo.addons.mail.tools.discuss import Store


class Message(models.Model):
    _inherit = 'mail.message'

    human_prompt_tokens = fields.Integer('Human Prompt Tokens')
    ai_completion_tokens = fields.Integer('AI Completion Tokens')
    cost_tokens = fields.Integer('Cost Tokens')
    # 是否ai回复
    is_ai = fields.Boolean('Is Ai', default=False)
    # 得到 ai 响应后，需要特殊处理ai的
    ai2model = fields.Char('Ai Response model')
    ai2id = fields.Integer('Ai Response id')

    def _to_store(
        self,
        store: Store,
        fields,
        *,
        format_reply=True,
        msg_vals=False,
        add_followers=False,
        followers=None,
    ):
        # Odoo 19: fields 为必传位置参数，移除 for_current_user，msg_vals 默认 False
        custom_fields = [
            'human_prompt_tokens',
            'ai_completion_tokens',
            'cost_tokens',
            'is_ai'
        ]
        merged_fields = list(set(list(fields) + custom_fields))
        return super()._to_store(store, merged_fields, format_reply=format_reply, msg_vals=msg_vals, add_followers=add_followers, followers=followers)
