# -*- coding: utf-8 -*-
import logging
from odoo import models, _
from odoo.addons.account.models.chart_template import template

_logger = logging.getLogger(__name__)


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
        # coa会计科目级，覆盖设置
        # 中国：小企业默认不给开 盎格鲁撒克逊会计，不开权责。  大企业关闭盎格鲁撒克逊会计（=不自动在销售出库时结转成本），用存货成本账+月结时结转出库成本处理
        return {
            'name': _('2027中国企业会计科目表-odoo20'),
            'code_digits': 4,
            # 不做存货账：关闭，小企业让其关闭开启，实际因为不开存货成本账，开启也无用.
            'anglo_saxon_accounting': False,
            'use_storno_accounting': False,
            # todo: begin 有问题，不该在此
            'cash_account_code_prefix': '1001',
            'bank_account_code_prefix': '1002',
            'transfer_account_code_prefix': '1003',
            # end 有问题
            'property_account_receivable_id': 'account_1122',
            'property_account_payable_id': 'account_2202',
            'property_account_income_categ_id': 'account_6001',
            'property_account_expense_categ_id': 'account_6401',
            # 默认销售预收款用 2203.02 服务的处理，每品类不同，故不在公司字段定义，原生是在品类中处理
            'property_account_downpayment_categ_id': 'account_2203',
            'property_account_prepay_categ_id': 'account_1123',
            'property_tax_receivable_account_id': 'account_2221_1_5',
            'property_tax_payable_account_id': 'account_2221_1_1',
            # 库存相关科目
            'property_stock_account_input_categ_id': 'account_1401',
            # 出库科目：发出商品，关闭自动存货凭证时 property_stock_account_output_categ_id 是无效的
            'property_stock_account_output_categ_id': 'account_1406',
            # 出库科目：存货过渡，开启自动存货凭证时用。最好新建 account_6401 下子科目 存货成本中转
            # 'property_stock_account_output_categ_id': 'account_1901',
            'property_stock_valuation_account_id': 'account_1405_01',
            'property_stock_account_production_cost_id': 'account_5001',
        }

    @template('cn_standard_smb')
    def _get_cn_standard_smb_template_data(self):
        # 小规模纳税人：科目结构与一般纳税人一致，去掉进项抵扣相关明细，税项用征收率
        # 科目表标识 code = cn_standard_smb（科目编码保持 4 位不变，模板记录 id 加 _smb 后缀）
        return {
            'name': _('2027中国企业会计科目表-小规模纳税人'),
            'code_digits': 4,
            'anglo_saxon_accounting': False,
            'use_storno_accounting': False,
            'cash_account_code_prefix': '1001',
            'bank_account_code_prefix': '1002',
            'transfer_account_code_prefix': '1003',
            'property_account_receivable_id': 'account_1122_smb',
            'property_account_payable_id': 'account_2202_smb',
            'property_account_income_categ_id': 'account_6001_smb',
            'property_account_expense_categ_id': 'account_6401_smb',
            'property_account_downpayment_categ_id': 'account_2203_smb',
            'property_account_prepay_categ_id': 'account_1123_smb',
            # 小规模不抵扣进项，税额统一挂销项税额 / 未交增值税
            'property_tax_receivable_account_id': 'account_2221_01_05_smb',
            'property_tax_payable_account_id': 'account_2221_02_smb',
            'property_stock_account_input_categ_id': 'account_1401_smb',
            'property_stock_account_output_categ_id': 'account_1406_smb',
            'property_stock_valuation_account_id': 'account_1405_01_smb',
            'property_stock_account_production_cost_id': 'account_5001_smb',
        }

    @template('cn_standard_smb', 'res.company')
    def _get_cn_standard_smb_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.cn',
                'cash_account_code_prefix': '1001',
                'bank_account_code_prefix': '1002',
                'transfer_account_code_prefix': '1003',
                'account_default_pos_receivable_account_id': 'account_1124_smb',
                # 默认销项按现行小规模 1% 征收率（价内税），采购侧不抵扣
                'account_sale_tax_id': 'l10n_cn_smb_sale_1_included',
                'account_purchase_tax_id': 'l10n_cn_smb_purchase_0',
                'income_currency_exchange_account_id': 'account_6061_01_smb',
                'expense_currency_exchange_account_id': 'account_6061_02_smb',
                'default_pos_receivable_account_id': 'account_1124_smb',
                'account_journal_suspense_account_id': 'account_1002_07_smb',
                'account_journal_payment_debit_account_id': 'account_1002_08_smb',
                'account_journal_payment_credit_account_id': 'account_1002_09_smb',
                'purchase_iap_account_id': 'account_2202_03_smb',
                'account_journal_suspense_pc_account_id': 'account_1002_10_smb',
                'expense_outstanding_account_id': 'account_1002_10_smb',
                'deferred_expense_account_id': 'account_1801_smb',
                'deferred_revenue_account_id': 'account_2401_smb',
                'default_cash_difference_income_account_id': 'account_6603_smb',
                'default_cash_difference_expense_account_id': 'account_6603_smb',
                'account_journal_early_pay_discount_gain_account_id': 'account_6603_smb',
                'account_journal_early_pay_discount_loss_account_id': 'account_6603_smb',
            },
        }

    @template('cn_standard_smb', 'account.journal')
    def _get_cn_standard_smb_account_journal(self):
        return {
            'cash': {
                'name': _('Cash on Hand'),
                'type': 'cash',
                'code': 'CASH',
                'default_account_id': 'account_1001_smb',
            },
            'bank': {
                'name': _('Bank'),
                'code': 'BANK',
                'default_account_id': 'account_1002_01_smb',
            },
        }

    @template('cn_standard', 'res.company')
    def _get_cn_standard_res_company(self):
        # 公司级，覆盖设置
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
                'income_currency_exchange_account_id': 'account_6061_01',
                'expense_currency_exchange_account_id': 'account_6061_02',
                'default_pos_receivable_account_id': 'account_1124',
                'account_journal_suspense_account_id': 'account_1002_07',
                'account_journal_payment_debit_account_id': 'account_1002_08',
                'account_journal_payment_credit_account_id': 'account_1002_09',
                # 采购预付过渡，应付账款-预付过渡
                'purchase_iap_account_id': 'account_2202_03',
                # 备用金备处理款，安装备用金模块后有效，但无该字段也不报错。实际可用原生 expense_outstanding_account_id
                'account_journal_suspense_pc_account_id': 'account_1002_10',
                'expense_outstanding_account_id': 'account_1002_10',
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
        # 日记账级，覆盖设置
        # o20: account.journal.code 为 NOT NULL 且 _compute_code 依赖 type，
        # cash 若无 type/code，预计算不会生成 code，创建时直接报缺少必填字段 code
        return {
            'cash': {
                'name': _('Cash on Hand'),
                'type': 'cash',
                'code': 'CASH',
                'default_account_id': 'account_1001'
            },
            'bank': {
                'name': _('Bank'),
                'type': 'bank',
                'code': 'BANK',
                'default_account_id': 'account_1002_01',
            },
        }

    @template('cn_standard_rz', 'account.account')
    def _get_cn_standard_rz_account_account(self):
        # 科目级，覆盖设置
        return {}
    
    # @template('cn_standard', 'account.account')
    # def _get_cn_standard_account_account(self):
    #     # 处理指定文件
    #     return self._parse_csv('xxx', 'account.account', module='l10n_cn_standard_latest')

    def _post_load_data(self, template_code, company, template_data):
        # 处理安装后
        if template_code == 'cn_standard':
            _logger.info(
                '_post_load_data: cn_standard on company %s (id=%s), '
                'chart_template=%s, template_data keys=%s',
                company.name, company.id, company.chart_template,
                list(template_data.keys()) if template_data else 'empty',
            )
        return super()._post_load_data(template_code, company, template_data)
