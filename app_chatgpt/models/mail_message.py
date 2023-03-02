# -*- coding: utf-8 -*-

from odoo import fields, models


class Message(models.Model):
    _inherit = "mail.message"

    def _message_add_reaction(self, content):
        super(Message, self)._message_add_reaction(content)
        if self.create_uid.gpt_id:
            # 处理反馈
            pass
