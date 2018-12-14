# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    short_name = fields.Char('Short Name')  # 简称


class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    _order = 'sequence, name'

    sequence = fields.Integer('Sequence', help="Used to order partner category")
