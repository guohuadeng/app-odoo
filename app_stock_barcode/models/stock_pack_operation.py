# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError
from odoo.exceptions import Warning

import logging

logger = logging.getLogger(__name__)


class PackOperation(models.Model):
    _inherit = "stock.pack.operation"

    weight = fields.Float(
        'Weight', digits=dp.get_precision('Stock Weight'), related='product_id.weight', readonly=True, store=True,
        help="The weight of the contents in Kg, not including any packaging, etc.")

    weight_done_subtotal = fields.Float(
        'Weight Done Subtotal', digits=dp.get_precision('Stock Weight'), compute='_compute_weight_done_subtotal', readonly=True, store=True,
        help="The weight of the contents in Kg, not including any packaging, etc.")

    @api.depends('weight', 'qty_done')
    def _compute_weight_done_subtotal(self):
        for rec in self:
            rec.weight_done_subtotal = rec.weight * rec.qty_done
