# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from .lib.WordsSearch import WordsSearch


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        self.ensure_one()
        search = WordsSearch()
        search.SetKeywords([])
        body = kwargs.get('body', False)
        body = search.Replace(text=body)
        kwargs.update({'body': body})
        return super(MailThread, self).message_post(**kwargs)
