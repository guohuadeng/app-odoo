# -*- coding: utf-8 -*-
from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    # 注意，coa 相关模型
    # TEMPLATE_MODELS = (
    #     'account.group',
    #     'account.account',
    #     'account.tax.group',
    #     'account.tax',
    #     'account.journal',
    #     'account.reconcile.model',
    #     'account.fiscal.position',
    # )

    @template('cn_standard')
    def _get_cn_standard_template_data(self):
        return {
            'name': _('2025中国企业会计科目表-odoo18'),
            'code_digits': 4,
            'use_storno_accounting': True,
            # todo: begin 有问题，不该在此
            'cash_account_code_prefix': '1001',
            'bank_account_code_prefix': '1002',
            'transfer_account_code_prefix': '1003',
            # end 有问题
            'property_account_receivable_id': 'account_1122',
            'property_account_payable_id': 'account_2202',
            'property_account_income_categ_id': 'account_6001',
            'property_account_expense_categ_id': 'account_6401',
            'property_tax_receivable_account_id': 'account_2221_1_5',
            'property_tax_payable_account_id': 'account_2221_1_1',
            # 库存相关科目
            'property_stock_account_input_categ_id': 'account_1401',
            'property_stock_account_output_categ_id': 'account_1406',
            'property_stock_valuation_account_id': 'account_1405_01',
            'property_stock_account_production_cost_id': 'account_1405_01',
        }

    @template('cn_standard', 'res.company')
    def _get_cn_standard_res_company(self):
        res = {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.cn',
                'cash_account_code_prefix': '1001',
                'bank_account_code_prefix': '1002',
                'transfer_account_code_prefix': '1003',
                'account_default_pos_receivable_account_id': 'account_1124',
                # todo: 以下很多未生效
                # 以外贸为基准，销售或进口货物的，无另有规定时，按13%
                'account_sale_tax_id': 'l10n_cn_standard_sale_included_13',
                'account_purchase_tax_id': 'l10n_cn_standard_purchase_included_13',
                'income_currency_exchange_account_id': 'account_6061',
                'expense_currency_exchange_account_id': 'account_6061',
                'default_pos_receivable_account_id': 'account_1124',
                'account_journal_suspense_account_id': 'account_1002_07',
                'account_journal_payment_debit_account_id': 'account_1002_08',
                'account_journal_payment_credit_account_id': 'account_1002_09',
                'deferred_expense_account_id': 'account_1801',
                'deferred_revenue_account_id': 'account_2401',
                #  现金差异收入
                'default_cash_difference_income_account_id': 'account_6603',
                #  现金差额费用
                'default_cash_difference_expense_account_id': 'account_6603',
                #  现金折扣收益科目
                'account_journal_early_pay_discount_gain_account_id': 'account_6603',
                #  现金折扣损失科目
                'account_journal_early_pay_discount_loss_account_id': 'account_6603',
            },
        }
        return res

    @template('cn_standard', 'account.journal')
    def _get_cn_account_journal(self):
        return {
            'cash': {
                'name': _('Cash on Hand'),
                'default_account_id': 'account_1001'
            },
            'bank': {
                'name': _('Bank'),
                'default_account_id': 'account_1002_01',
            },
        }

    # @template('cn_standard', 'account.account')
    # def _get_cn_standard_account_account(self):
    #     # 处理指定文件
    #     return self._parse_csv('xxx', 'account.account', module='l10n_cn_standard_latest')

    def _post_load_data(self, template_code, company, template_data):
        # 处理安装后
        if template_code == 'cn_standard':
            pass
        res = super()._post_load_data(template_code, company, template_data)
        return res
