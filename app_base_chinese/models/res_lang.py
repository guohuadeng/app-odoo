# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResLang(models.Model):
    _inherit = 'res.lang'
    _order = 'active desc,sequence,name desc'
    
    sequence = fields.Integer('Sequence', help='Determine the display order', default=99)
