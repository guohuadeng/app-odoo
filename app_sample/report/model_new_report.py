# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.

#    Create on 2023-10-06
##############################################################################

from odoo import fields, models
from odoo.tools.sql import SQL, drop_view_if_exists


class ModelNewReport(models.Model):

    #  Model New Analysis
    _name = 'model.new.report'
    _auto = False
    _description = 'Model New Analysis'
    _rec_name = 'name'

    # Base field
    name = fields.Char(string='Name', readonly=True)
    ref = fields.Char(string='Reference', readonly=True)
    amount = fields.Float(string="Amount", readonly=True)
    date = fields.Datetime(string="Date", readonly=True)
    user_id = fields.Many2one('res.users', string='User', readonly=True)
    user_login = fields.Char(string='User Login', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    active = fields.Boolean(string="Active", readonly=True)

    # v20 断点：报表模型的 _select()/_from()/_join()/_where() 四个 SQL 文本钩子已从框架
    # 删除，原生改成 TableSQL 架构 —— 一个 _table_sql 属性返回 SQL 对象，init() 里
    # CREATE OR REPLACE VIEW（范式：addons/hr_timesheet/report/
    # timesheets_analysis_report.py:40 属性 + :74 init；聚合类报表见
    # addons/purchase/report/purchase_report.py:54 _table_sql + :60 _select_list）。
    # 旧写法里那四个方法在 v20 变成无人调用的普通方法，视图不会被创建，
    # report/model_new_report_views.xml 的 graph/pivot/list/search 四张视图会全部落空。
    # 下面 SQL 本体与 v18 逐字对应（同表同别名、同为 INNER JOIN res_users）。
    # 注意 _table_sql 要自带括号：它被 ORM 当 FROM 位置的表表达式用
    # （orm/query.py:64），原生 hr_timesheet 同样是 SQL("(%s %s %s)", ...)。
    @property
    def _table_sql(self) -> SQL:
        return SQL("""(
            SELECT
                m.id AS id,
                m.name AS name,
                m.ref AS ref,
                m.amount AS amount,
                m.date AS date,
                m.user_id AS user_id,
                u.login AS user_login,
                m.company_id AS company_id,
                m.active AS active
            FROM model_new AS m
            JOIN res_users AS u ON m.user_id = u.id
        )""")

    def init(self):
        drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            SQL("CREATE OR REPLACE VIEW %s AS (%s)", SQL.identifier(self._table), self._table_sql)
        )
