# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mixin.name.en']

    name_en_US = fields.Char('SPU English Name',
                             help='Standard English name. Used for customs declaration, international trade import/export and other business scenarios.')