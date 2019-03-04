# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    _order = 'sequence, name'

    sequence = fields.Integer('Sequence', help="Used to order partner category")
