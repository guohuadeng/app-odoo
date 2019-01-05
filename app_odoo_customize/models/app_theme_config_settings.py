# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

# 为兼容而保留
class AppThemeConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'app.theme.config.settings'
