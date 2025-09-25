# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResLang(models.Model):
    _inherit = 'res.lang'

    def _get_date_format_selection(self):
        current_year = fields.Date.today().year
        return [
            ('%Y-%m-%d', '%s-01-31' % current_year),
            ('%d/%m/%Y', '01/31/%s' % current_year),
            ('%m/%d/%Y', '31/01/%s' % current_year),
            ('%Y/%m/%d', '%s/31/01' % current_year),
            ('%d-%m-%Y', '01-31-%s' % current_year),
            ('%m-%d-%Y', '31-01-%s' % current_year),
            ('%Y-%m-%d', '%s-31-01' % current_year),
        ]

    time_format = fields.Selection(selection_add=[
        ('%H:%M', '13:00'),
        ('%I:%M:%S %p',)], ondelete={'%H:%M': 'set default'})

