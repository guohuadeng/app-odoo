# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    _inherit = "product.category"

