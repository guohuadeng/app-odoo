# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools

class AccountTaxGroup(models.Model):
    _inherit = 'account.tax.group'

    active = fields.Boolean(default=True, help="Set active to false to hide the tax without removing it.")

