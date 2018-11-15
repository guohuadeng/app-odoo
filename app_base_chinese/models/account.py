# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.model
    def _search_new_account_code(self, company, digits, prefix):
        for num in range(1, 100):
            new_code = str(prefix.ljust(digits - 1, '0')) + str(num)
            rec = self.search([('code', '=', new_code), ('company_id', '=', company.id)], limit=1)
            if not rec:
                return new_code
        raise UserError(_('Cannot generate an unused account code.'))

