# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_sale_weight_print = fields.Boolean("Show Weight in Sale Print", implied_group='app_product_weight_sale.group_sale_weight_print')
