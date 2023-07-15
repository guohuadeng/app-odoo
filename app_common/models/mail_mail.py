# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class MailMail(models.Model):
    _inherit = "mail.mail"
    
    # 猴子补丁模式，改默认发邮件逻辑
    def _send(self, auto_commit=False, raise_exception=False, smtp_session=None):
        for m in self:
            if m.email_to and (m.email_to.find('example.com') != -1 or m.email_to.find('@odooai.cn') != -1 or m.email_to.find('@odooapp.cn') != -1):
                self = self - m
        return super(MailMail, self)._send(auto_commit, raise_exception, smtp_session)
