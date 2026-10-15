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
    # v20：recursive 参数在 ORM 重构后仍是正式字段属性（odoo/orm/fields.py 文档 :param bool recursive
    # 与 Field.recursive），自引用依赖必须显式声明，否则会打出
    # "Field ... should be declared with recursive=True" 警告且递归计算顺序不保证。故保留 recursive=True。
    child_all_count = fields.Integer('Indirect Surbordinates Count', store=False, recursive=True,
                                     compute='_compute_child_all_count')

    image_128 = fields.Image(related='product_id.image_128', readonly=True)
    # v20 原生 mrp.production 已提供 product_name（compute='_compute_product_name'，
    # 见 addons/mrp/models/mrp_production.py），原 related='product_id.name' 覆写会把原生
    # compute 一并带上，触发 "Field ... is both compute and related" 警告并改变原生显示口径，
    # 本模块视图未引用该字段，故 v20 下不再覆写。
    parent_path = fields.Char(index=True)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)

    @api.model_create_multi
    def create(self, vals_list):
        # 配置层级关系
        for vals in vals_list:
            if 'origin' in vals and vals['origin']:
                mo = self.env['mrp.production'].search([('name', '=', vals['origin'])], limit=1, order='id desc')
                if len(mo) == 1:
                    vals['parent_id'] = mo[0].id
        res = super(MrpProduction, self).create(vals_list)
        return res
