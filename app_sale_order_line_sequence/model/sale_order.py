# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    max_line_sequence = fields.Integer(string='Max sequence in lines')

    @api.multi
    def _reset_sequence(self):
        for rec in self:
            current_sequence = 0
            for line in rec.order_line:
                current_sequence += 1
                line.sequence = current_sequence
            rec.max_line_sequence = current_sequence

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        recal = False
        if vals.get('order_line') and vals['order_line']:
            # todo: 优化，只有order_line中有 sequence 时才重算
            for line in vals['order_line']:
                if line[2] and 'sequence' in line[2]:
                    recal = True
                    break
        if recal:
            for rec in self:
                rec._reset_sequence()
                pass
        return res

    @api.model
    def create(self, vals):
        if vals.get('order_line') and vals['order_line']:
            current_sequence = 0
            for line in vals['order_line']:
                if line[2]:
                    current_sequence += 1
                    line[2].update({'sequence': current_sequence})
        return super(SaleOrder, self).create(vals)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # displays sequence on the order line
    sequence2 = fields.Integer(
        help="Shows the sequence of this line in the sale order.",
        related='sequence',
        string="Line Number",
        readonly=True,
        store=True
    )
