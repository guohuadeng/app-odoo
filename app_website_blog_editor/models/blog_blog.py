# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class BlogBlog(models.Model):
    _inherit = 'blog.blog'
    _order = 'sequence, name'

    seo_name = fields.Char(tracking=True)
    
    # 排序
    sequence = fields.Integer(string='Sequence', default=20, index=True, help="Determine the display order")

    def action_view_blog_post(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').read()[0]
        action['domain'] = [('blog_id', '=', self.id)]
        return action

    # def unlink(self):
    #     # active的先不删除，设置为 deactive
    #     to_deactive = self.filtered(lambda r: r.active)
    #     self = self - to_deactive
    #     to_deactive.write({
    #         'active': False,
    #     })
    #     if self:
    #         return super(BlogBlog, self).unlink()
    #     else:
    #         return False
