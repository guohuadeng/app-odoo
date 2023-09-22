# -*- coding: utf-8 -*-

from odoo import fields, models


class Message(models.Model):
    _inherit = "mail.message"

    human_prompt_tokens = fields.Integer('Human Prompt Tokens')
    ai_completion_tokens = fields.Integer('AI Completion Tokens')
    cost_tokens = fields.Integer('Cost Tokens')
    # 是否ai回复
    is_ai = fields.Boolean('Is Ai', default=False)

    def _message_add_reaction(self, content):
        super(Message, self)._message_add_reaction(content)
        if self.create_uid.gpt_id:
            # 处理反馈
            pass

    def message_format(self, format_reply=True):
        message_values = super(Message, self).message_format(format_reply=format_reply)

        for message in message_values:
            message_sudo = self.browse(message['id']).sudo().with_prefetch(self.ids)
            message['human_prompt_tokens'] = message_sudo.human_prompt_tokens
            message['ai_completion_tokens'] = message_sudo.ai_completion_tokens
            message['cost_tokens'] = message_sudo.cost_tokens
            message['is_ai'] = message_sudo.is_ai
        return message_values
