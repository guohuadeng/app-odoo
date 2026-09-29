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

    def _message_reaction(self, content, action, partner, guest, store=None):
        # Odoo20: 原 _message_add_reaction(content) 已改为 _message_reaction
        res = super(Message, self)._message_reaction(content, action, partner, guest, store=store)
        if self.create_uid.gpt_id:
            # 处理反馈
            pass
        return res

    def _store_message_fields(self, res, *, format_reply=True, chatter_fields=False,
                              inbox_fields=False, followers=None):
        # Odoo20: 原 _to_store 重写已废弃，改为在 Store 字段方法中追加自定义字段
        res.extend(['human_prompt_tokens', 'ai_completion_tokens', 'cost_tokens', 'is_ai'])
        return super()._store_message_fields(
            res,
            format_reply=format_reply,
            chatter_fields=chatter_fields,
            inbox_fields=inbox_fields,
            followers=followers,
        )
