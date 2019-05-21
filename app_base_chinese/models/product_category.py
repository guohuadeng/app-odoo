# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class ProductCategory(models.Model):
    _inherit = "product.category"

    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True, translate=True)
