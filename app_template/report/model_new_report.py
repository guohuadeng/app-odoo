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

from odoo import fields, models, tools, api


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

    @api.model
    def _select(self):
        return '''
            SELECT
                m.id,
                m.name,
                m.ref,
                m.amount,
                m.date,
                m.user_id,
                u.login AS user_login,
                m.company_id,
                m.active
        '''

    @api.model
    def _from(self):
        return '''
            FROM model_new AS m
        '''

    @api.model
    def _join(self):
        return '''
            JOIN res_users AS u ON m.user_id = u.id
        '''

    @api.model
    @api.model
    def _where(self):
        return ''

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        sql = '''
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
                %s
                %s
            )
        ''' % (self._table, self._select(), self._from(), self._join(), self._where())
        self._cr.execute(sql)
