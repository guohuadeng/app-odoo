# -*- coding: utf-8 -*-

# Created on 2018-11-07
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    @api.model
    def _prepare_transfer_account_template(self):
        # 初始化时，使用 _load 方法，不再使用此方法了
        ''' Prepare values to create the transfer account that is an intermediary account used when moving money
        from a liquidity account to another.

        :return:    A dictionary of values to create a new account.account.
        '''
        # 分隔符，金蝶为 "."，用友为""，注意odoo中一级科目，现金默认定义是4位头，银行是6位头
        delimiter = '.'
        digits = self.code_digits
        prefix = self.transfer_account_code_prefix or ''
        # Flatten the hierarchy of chart templates.
        chart_template = self
        chart_templates = self
        while chart_template.parent_id:
            chart_templates += chart_template.parent_id
            chart_template = chart_template.parent_id
        new_code = ''
        for num in range(1, 100):
            new_code = str(prefix.ljust(digits - 1, '0')) + delimiter + '%02d' % (num)
            rec = self.env['account.account.template'].search(
                [('code', '=', new_code), ('chart_template_id', 'in', chart_templates.ids)], limit=1)
            if not rec:
                break
        else:
            raise UserError(_('Cannot generate an unused account code.'))
        return {
            'name': _('Liquidity Transfer'),
            'code': new_code,
            'account_type': 'asset_current',
            'reconcile': True,
            'chart_template_id': self.id,
        }

    def _load(self, company):
        if self == self.env.ref('l10n_cn_standard_latest.l10n_chart_china_standard_business_latest', False):
            # #todo: 当为 标准中国会计的处理
            # company.write({
            #     'account_journal_suspense_account_id': self.account_journal_suspense_account_id.id if self.account_journal_suspense_account_id else False,
            #     'account_journal_payment_credit_account_id': self.account_journal_payment_credit_account_id.id if self.account_journal_payment_credit_account_id else False,
            #     'account_journal_payment_debit_account_id': self.account_journal_payment_debit_account_id.id if self.account_journal_payment_debit_account_id else False,
            # })
            pass
        res = super(AccountChartTemplate, self)._load(company)
        # todo: 更新已有res.partner 的字段（当原值为空时） 应收账款 = chart.property_account_receivable_id，应付账款=property_account_payable_id
        # 更新父级
        company = self.env.user.company_id
        acc_ids = self.env['account.account'].sudo().search([('company_id', '=', company.id)])
        for acc in acc_ids:
            code = acc.code
            todo_account = self.env['account.account.template'].sudo().search([
                ('code', '=', code),
                ('chart_template_id', '=', self.id),
                ('parent_id', '!=', False)
            ], limit=1)
            if len(todo_account) or code == '2221.01.01':
                parent_code = todo_account[0].parent_id.code
                if parent_code:
                    parent = self.env['account.account'].sudo().search([
                        ('company_id', '=', company.id),
                        ('code', '=', parent_code),
                    ], limit=1).exists()
                    if parent:
                        acc.write({
                            'parent_id': parent.id,
                        })
        return res


