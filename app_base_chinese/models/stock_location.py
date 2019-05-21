# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class Location(models.Model):
    _inherit = "stock.location"

    complete_name = fields.Char("Full Location Name", compute='_compute_complete_name', store=True, translate=True)
