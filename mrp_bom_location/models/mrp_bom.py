# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    location_id = fields.Many2one(
        string='Location',
        comodel_name='stock.location',
    )

    @api.onchange('picking_type_id')
    def _onchange_picking_type_id(self):
        if (self.picking_type_id and
                self.picking_type_id.default_location_src_id):
            self.location_id = self.picking_type_id.default_location_src_id


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    location_id = fields.Many2one(
        related='bom_id.location_id',
        readonly=True,
        store=True,
    )
