# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'

    def app_set_to_odooai_cn(self):
        for rec in self:
            if rec.country_id.code == 'CN' and rec.chart_template != 'cn_standard':
                has_accounting_entries = rec.root_id._existing_accounting()
                if not has_accounting_entries:
                    # 处理额外的本年收益
                    unaffected_earnings_type = "equity_unaffected"
                    account = self.env['account.account'].with_company(rec).search([
                        *self.env['account.account']._check_company_domain(rec),
                        ('account_type', '=', unaffected_earnings_type),
                    ], limit=1)
                    if account:
                        account.unlink()
                    rec.chart_template = 'cn_standard'
                    self.env['account.chart.template'].try_loading(rec.chart_template, company=rec)
