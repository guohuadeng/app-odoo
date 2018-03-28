# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    picking_type_group_id = fields.Many2one('stock.picking.type.group', 'Picking Type Group')

