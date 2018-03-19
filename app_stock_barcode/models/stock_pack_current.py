# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp

import logging
logger = logging.getLogger(__name__)

class StockPackCurrent(models.Model):
    _name = "stock.pack.current"
    _description = "Current Packing Operation"
    _order = "id desc"

    picking_id = fields.Many2one(
        'stock.picking', 'Stock Picking',
        required=True, ondelete="cascade",
        help='The stock operation where the packing has been made')
    product_id = fields.Many2one('product.product', 'Product', ondelete="cascade")
    product_uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    product_qty = fields.Float('To Do', default=0.0, digits=dp.get_precision('Product Unit of Measure'), required=True)
    qty_done = fields.Float('Done', default=0.0, digits=dp.get_precision('Product Unit of Measure'))
    package_id = fields.Many2one('stock.quant.package', 'Source Package')
    result_package_id = fields.Many2one(
        'stock.quant.package', 'Destination Package',
        ondelete='cascade', required=False,
        help="If set, the operations are packed into this package")

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

