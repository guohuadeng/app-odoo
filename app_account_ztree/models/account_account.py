# -*- coding: utf-8 -*-

# Created on 2018-11-28
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
from odoo.exceptions import UserError, ValidationError

class AccountAccount(models.Model):
    _inherit = ['account.account']
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'code'
    # _rec_name = 'complete_name'

    parent_id = fields.Many2one('account.account', 'Parent Chart', index=True, ondelete='cascade')
    child_ids = fields.One2many('account.account', 'parent_id', 'Child Chart')
    parent_path = fields.Char(index=True)
    # todo: view 类型只用于上级，不可在凭证中选择使用。  odoo 中使用 _compute_account_type 处理是找不到自动设置为 其上级科目
    # 故暂时不增加此类型
    # account_type = fields.fields.Selection(selection_add=[
    #     ('view', 'View Only'),
    # ])

    @api.model
    def _search_new_account_code(self, start_code, cache=None):
        # 分隔符，金蝶为 "."，用友为""，注意odoo中一级科目，现金默认定义是4位头，银行是6位头
        # 在 odoo18已优化可处理
        """
            Examples:
                |  start_code  |  codes checked for availability                            |
                +--------------+------------------------------------------------------------+
                |    102100    |  102101, 102102, 102103, 102104, ...                       |
                |     1598     |  1599, 1600, 1601, 1602, ...                               |
                |   10.01.08   |  10.01.09, 10.01.10, 10.01.11, 10.01.12, ...               |
                |   10.01.97   |  10.01.98, 10.01.99, 10.01.97.copy2, 10.01.97.copy3, ...   |
                |    1021A     |  1021A, 1022A, 1023A, 1024A, ...                           |
                |    hello     |  hello.copy, hello.copy2, hello.copy3, hello.copy4, ...    |
                |     9998     |  9999, 9998.copy, 9998.copy2, 9998.copy3, ...              |
        """
        res = super()._search_new_account_code(start_code, cache)
        return res

    def refresh_account_parent(self, company=None):
        if not company:
            company = self.env.user.company_id
        self = self.filtered(lambda r: len(r.code) > 2).sorted(key=lambda r: r.code)
        done = 0
        # 分隔符 delimiter，用友为""，金蝶为 "."，注意odoo中一级科目，现金默认定义是4位头，银行是6位头
        # 我们使用 用友的多级科目方式，自动生成下级，此处直接覆盖原生
        delimiter = company.coa_delimiter or ''
        for rec in self:
            if len(rec.code) > 2:
                p_code = rec.code[:len(rec.code) - 2]
                if delimiter and delimiter != '':
                    p_code = rec.code[:len(rec.code) - 2 - len(delimiter)]
                p_acc = self.search([('company_ids', '=', company.id), ('code', '=', p_code)])
                if p_acc and rec.parent_id != p_acc:
                    rec.write({'parent_id': p_acc.id})
                    done += 1

        return {
            'effect': {
                'fadeout': 'fast',
                'message': _('Update parent account chart done.<br/>【%s】 records updated.' % done),
                'img_url': '/web/image/%s/%s/image_1024' % (self.env.user._name,
                                                            self.env.user.id) if self.env.user.image_1024 else '/web/static/src/img/smile.svg',
                'type': 'rainbow_man',
            }
        }
