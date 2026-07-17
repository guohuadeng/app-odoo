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
                    # 注意：不要在此处手动设置 chart_template，
                    # 让 try_loading -> _load() 内部设置，
                    # 否则 reload_template=True 会触发 _pre_reload_data 清空数据，
                    # 导致 res.company 配置和 property_* 字段无法写入
                    _logger.info(
                        'Loading cn_standard chart template for company %s (current chart_template=%s)',
                        rec.name, rec.chart_template,
                    )
                    self.env['account.chart.template'].try_loading('cn_standard', company=rec)
