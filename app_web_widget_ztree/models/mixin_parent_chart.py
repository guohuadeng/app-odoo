# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from odoo import api, fields, models, _


# 用于widget的树结构 mixin
class MixinParentChart(models.AbstractModel):
    _name = 'mixin.parent.chart'
    _description = '树状结构基础mixin'

    _parent_name = "parent_id"
    _parent_store = True
    _order = 'parent_path asc'
    _parent_order = 'id'

    # 上级生产单
    parent_id = fields.Many2one(_name, string='上级对象', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(_name, 'parent_id', string='结构树')
