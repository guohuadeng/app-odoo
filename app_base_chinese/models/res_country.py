# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Country(models.Model):
    _inherit = 'res.country'
    _order = 'sequence,name'

    sequence = fields.Integer('Sequence', help="Determine the display order", default=99)
