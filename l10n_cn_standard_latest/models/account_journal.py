# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


# 调整初始化算法
class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.model
    def _prepare_liquidity_account(self, name, company, currency_id, type):
        digits = 6
        chart = self.company_id.chart_template_id
        if chart:
            digits = int(chart.code_digits)
        # Seek the next available number for the account code
        if type == 'bank':
            account_code_prefix = company.bank_account_code_prefix or ''
        else:
            account_code_prefix = company.cash_account_code_prefix or company.bank_account_code_prefix or ''
        digits = len(account_code_prefix)
        # 获取上级
        p_account = self.env['account.account'].search([('code', '=', account_code_prefix), ('company_id', '=', company.id)], limit=1)

        return {
            'name': name,
            'currency_id': currency_id or False,
            'code': self.env['account.account']._search_new_account_code(company, digits, account_code_prefix),
            'account_type': 'asset_cash',
            'parent_id': p_account and p_account.id or False,
            'group_id': p_account and p_account.group_id and p_account.group_id.id or False,
            'company_id': company.id,
        }
