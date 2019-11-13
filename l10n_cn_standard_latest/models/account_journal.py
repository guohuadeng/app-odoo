# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


# 调整初始化算法
class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.model
    def _prepare_liquidity_account(self, name, company, currency_id, type):
        '''
        This function prepares the value to use for the creation of the default debit and credit accounts of a
        liquidity journal (created through the wizard of generating COA from templates for example).

        :param name: name of the bank account
        :param company: company for which the wizard is running
        :param currency_id: ID of the currency in which is the bank account
        :param type: either 'cash' or 'bank'
        :return: mapping of field names and values
        :rtype: dict
        '''
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

        liquidity_type = self.env.ref('account.data_account_type_liquidity')
        return {
            'name': name,
            'currency_id': currency_id or False,
            'code': self.env['account.account']._search_new_account_code(company, digits, account_code_prefix),
            'user_type_id': liquidity_type and liquidity_type.id or False,
            'company_id': company.id,
        }
