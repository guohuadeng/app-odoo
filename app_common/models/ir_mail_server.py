# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import re
import logging
_logger = logging.getLogger(__name__)

class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'
    _order = 'sequence'
    
    # 改默认发邮件逻辑
    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None,
                   smtp_ssl_certificate=None, smtp_ssl_private_key=None,
                   smtp_debug=False, smtp_session=None):
        email_to = message['To']
        
        # 忽略掉无效email，避免被ban
        if email_to:
            BLOCK_EMAIL_PATTERNS = [
                re.compile(r'example\.com'),                     # 阻止包含example.的邮箱
                re.compile(r'@sunpop\.cn'),                   # 阻止sunpop.cn域名
                re.compile(r'@odooapp\.cn'),                  # 阻止odooapp.cn域名
            ]
            
            # 检查是否匹配阻止的邮箱模式
            is_blocked = any(pattern.search(email_to) for pattern in BLOCK_EMAIL_PATTERNS)
            
            if is_blocked:
                _logger.warning(_("=================Email to ignore: %s") % email_to)
                raise AssertionError(_("Email to ignore: %s") % email_to)

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_ssl_certificate, smtp_ssl_private_key,
                                                    smtp_debug, smtp_session)
