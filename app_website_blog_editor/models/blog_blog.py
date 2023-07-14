# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class BlogBlog(models.Model):
    _inherit = 'blog.blog'
    _order = 'sequence, name'
    
    # 排序
    sequence = fields.Integer(string='Sequence', default=20, index=True, help="Determine the display order")

    def action_view_blog_post(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').read()[0]
        action['domain'] = [('blog_id', '=', self.id)]
        return action
