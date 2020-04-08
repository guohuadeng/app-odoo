# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # 注意，res.partner 有 parent_id 和 child_ids
    _parent_name = "parent_id"
    _parent_store = True

    # 上级生产单
    parent_id = fields.Many2one('mrp.production', 'Parent Manufacturing', index=True, ondelete='cascade',
        help="The parent manufacturing orders that generate this order. Follow the rule of multi level bom.")
    child_ids = fields.One2many('mrp.production', 'parent_id', string='Sub Manufacturing')
    child_all_count = fields.Integer('Indirect Surbordinates Count', store=False,
                                     compute='_compute_child_all_count')

    image_128 = fields.Binary(related='product_id.image_small', readonly=True)
    product_name = fields.Char(related='product_id.name', readonly=True)
    parent_path = fields.Char(index=True)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)

    @api.model
    def create(self, values):
        # 配置层级关系
        if 'origin' in values and values['origin']:
            mo = self.env['mrp.production'].search([('name', '=', values['origin'])])
            if len(mo) == 1:
                values['parent_id'] = mo.id
        res = super(MrpProduction, self).create(values)
        return res
