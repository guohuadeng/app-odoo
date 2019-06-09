# -*- coding: utf-8 -*-

from collections import namedtuple
import json
import time

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError


class PickingTypeGroup(models.Model):
    _name = "stock.picking.type.group"
    _description = "Group the picking view"
    _order = 'sequence, id'

    name = fields.Char('Picking Type Group Name', required=True, translate=True)
    color = fields.Integer('Color')
    sequence = fields.Integer('Sequence', help="Used to order the 'All Operations' kanban view")
    active = fields.Boolean('Active', default=True)
