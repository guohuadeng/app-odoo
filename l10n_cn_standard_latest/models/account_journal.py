# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


# 调整初始化算法
class AccountJournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _prepare_liquidity_account_vals(self, company, code, vals):
        res = super()._prepare_liquidity_account_vals(company, code, vals)
        # 分隔符，金蝶为 "."，用友为""，注意odoo中一级科目，现金默认定义是4位头，银行是6位头
        delimiter = '.'
        if hasattr(company, 'coa_delimiter'):
            delimiter = company.coa_delimiter
        code = code + delimiter + '01'
        new_code = self.env['account.account']._search_new_account_code(code)
        res.update({'code': new_code})
        return res
