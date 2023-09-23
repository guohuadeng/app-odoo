# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class BlogTag(models.Model):
    _inherit = 'blog.tag'
    _order = 'sequence, name'
    
    # 排序
    sequence = fields.Integer(string='Sequence', default=20, index=True, help="Determine the display order")
