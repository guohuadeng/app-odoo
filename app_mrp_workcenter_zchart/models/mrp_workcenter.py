# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)


class MrpWorkCenter(models.Model):
    _inherit = 'mrp.workcenter'

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
    level = fields.Integer('Level', compute='_compute_level', inverse='_set_level', default=0, store=True)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)


    @api.onchange('parent_id')
    def _onchange_level(self):
        level = 0
        if self.parent_id:
            level = self.parent_id.level + 1
        self.level = level

    @api.depends('parent_id', 'parent_id.level')
    def _compute_level(self):
        for rec in self:
            level = 0
            if rec.parent_id:
                level = rec.parent_id.level + 1
            rec.level = level

    def _set_level(self):
        pass
