# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Location(models.Model):
    _name = "stock.location"
    _inherit = ['stock.location', 'image.mixin']
