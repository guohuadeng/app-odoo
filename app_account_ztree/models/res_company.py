# -*- coding: utf-8 -*-

from datetime import timedelta, datetime, date
import calendar

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError, RedirectWarning
from odoo.tools.mail import is_html_empty
from odoo.tools.misc import format_date
from odoo.tools.float_utils import float_round, float_is_zero
from odoo.addons.account.models.account_move import MAX_HASH_VERSION


class ResCompany(models.Model):
    _inherit = ['res.company']

    coa_delimiter = fields.Char(string='COA Delimiter', readonly=False, default='.',
                                help='Delimiter after parent account in Chart of Accounts')
