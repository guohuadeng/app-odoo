# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    virtual_available = fields.Float(
        related='product_id.virtual_available',
        readonly=True,
    )
    qty_available = fields.Float(
        related='product_id.qty_available',
        readonly=True,
    )
