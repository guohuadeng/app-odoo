# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)


class MrpWorkCenter(models.Model):
    _name = 'mrp.workcenter'
    _inherit = ['mrp.workcenter', 'image.mixin']

    # 建立层级关系
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'code'

    parent_id = fields.Many2one('mrp.workcenter', 'Parent WC', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('mrp.workcenter', 'parent_id', 'Child WCs')
    child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_child_all_count', store=False)
    parent_path = fields.Char(index=True)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)

