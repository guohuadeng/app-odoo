# -*- coding: utf-8 -*-

# Created on 2018-11-07
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

from odoo import api, fields, models, exceptions, _

class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    def _get_account_vals(self, company, account_template, code_acc, tax_template_ref):
        res = super(AccountChartTemplate, self)._get_account_vals(company, account_template, code_acc, tax_template_ref)
        if account_template.parent_id:
            parent_account = self.env['account.account'].sudo().search([
                '&',
                ('code', '=', account_template.parent_id.code),
                ('company_id', '=', company.id)
            ], limit=1)
            res.update({
                'parent_id': parent_account.id,
            })
        return res

    

