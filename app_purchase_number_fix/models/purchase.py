# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero, float_compare
from odoo.exceptions import UserError, AccessError
from odoo.tools.misc import formatLang
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
import odoo.addons.decimal_precision as dp


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.depends('order_line.move_ids.state',
                 'order_line.move_ids.picking_id',
                 'order_line.move_ids.returned_move_ids',
                 'order_line.move_ids.returned_move_ids.returned_move_ids')
    def _compute_picking(self):
        for order in self:
            pickings = self.env['stock.picking']
            for line in order.order_line:
                # We keep a limited scope on purpose. Ideally, we should also use move_orig_ids and
                # do some recursive search, but that could be prohibitive if not done correctly.
                return_moves = line.move_ids.mapped('returned_move_ids')
                moves = line.move_ids | return_moves | return_moves.mapped('returned_move_ids')
                moves = moves.filtered(lambda r: r.state != 'cancel')
                pickings |= moves.mapped('picking_id')
            order.picking_ids = pickings
            order.picking_count = len(pickings)

    @api.depends('order_id.state',
                 'move_ids.state',
                 'move_ids.returned_move_ids.state',
                 'move_ids.returned_move_ids.returned_move_ids.state')
    def _compute_qty_received(self):
        for line in self:
            if line.order_id.state not in ['purchase', 'done']:
                line.qty_received = 0.0
                continue
            if line.product_id.type not in ['consu', 'product']:
                line.qty_received = line.product_qty
                continue
            total = 0.0
            return_moves = line.move_ids.mapped('returned_move_ids')
            moves = line.move_ids | return_moves | return_moves.mapped('returned_move_ids')

            for move in moves:
                value = 0.0
                if move.state == 'done':
                    value = move.product_uom._compute_quantity(move.product_uom_qty, line.product_uom)
                    if move.location_id.usage == 'supplier':
                        total += value
                    else:
                        total -= value
            line.qty_received = total
