# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from .lib.WordsSearch import WordsSearch


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    # todo: 不是说在此屏蔽，而是当用户发出敏感词时，提示下，同时不发送到 ai
    # @api.returns('mail.message', lambda value: value.id)
    # def message_post(self, **kwargs):
        
        # self.ensure_one()
        # search = WordsSearch()
        # search.SetKeywords([])
        # body = kwargs.get('body', False)
        # body = search.Replace(text=body)
        # kwargs.update({'body': body})
        # return super(MailThread, self).message_post(**kwargs)
