# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

# v20 断点：旧 osv 包（expression 所在处）整包删除。
# v20 把 domain 表达收敛到 odoo.orm.Domain，原来的 expression.OR(domains)
# 等价于 Domain.OR(domains)（orm/domains.py:307，与 v20 原生
# account/models/account_account.py:470 的写法一致）。
#
# 注意导入路径：Domain 是从 odoo.fields 转出的，不是 odoo.orm
# —— `from odoo.orm import Domain` 会 ImportError，
# 与 v20 原生 account/models/account_account.py:10 的 `from odoo.fields import Domain` 一致。
from odoo.fields import Domain

try:
    from cn2an import an2cn
except ImportError:
    an2cn = None

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def check_cn2an(self):
        return an2cn

    @api.model
    def _convert_to_amount_in_word(self, number):
        """Convert number to ``amount in words`` for Chinese financial usage."""
        if not self.check_cn2an():
            return None
        return an2cn(number, 'rmb')

    def _count_attachments(self):
        domains = [[('res_model', '=', 'account.move'), ('res_id', '=', self.id)]]
        statement_ids = self.line_ids.mapped('statement_id')
        payment_ids = self.line_ids.mapped('payment_id')
        if statement_ids:
            domains.append([('res_model', '=', 'account.bank.statement'), ('res_id', 'in', statement_ids.ids)])
        if payment_ids:
            domains.append([('res_model', '=', 'account.payment'), ('res_id', 'in', payment_ids.ids)])
        return self.env['ir.attachment'].search_count(Domain.OR(domains))
