# -*- coding: utf-8 -*-
from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('cn_standard')
    def _get_cn_standard_template_data(self):
        return {
            'name': _('2024中国企业会计科目表-odoo17'),
            'code_digits': 4,
            'property_account_receivable_id': 'account_1122',
            'property_account_payable_id': 'account_2202',
            'property_account_expense_categ_id': 'account_6401',
            'property_account_income_categ_id': 'account_6001',
        }

    @template('cn_standard', 'res.company')
    def _get_cn_standard_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.cn',
                'bank_account_code_prefix': '1002',
                'cash_account_code_prefix': '1001',
                'transfer_account_code_prefix': '1003',
                'account_default_pos_receivable_account_id': 'account_1124',
                'income_currency_exchange_account_id': 'account_6051',
                'expense_currency_exchange_account_id': 'account_6711',
                'account_sale_tax_id': 'l10n_cn_standard_sale_included_13',
                'account_purchase_tax_id': 'l10n_cn_standard_purchase_excluded_13',
            },
        }
    
    @template('cn_standard', 'account.journal')
    def _get_cn_account_journal(self):
        return {
            'cash': {
                'name': 'Cash on Hand',
                'default_account_id': 'account_1001'
            },
            'bank': {
                'default_account_id': 'account_1002',
            },
        }
