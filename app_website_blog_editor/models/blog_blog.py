# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class BlogBlog(models.Model):
    _inherit = 'blog.blog'
    _order = 'sequence, name'
    
    # 排序
    sequence = fields.Integer(string='Sequence', default=20, index=True, help="Determine the display order")
