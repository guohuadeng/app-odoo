# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class BlogPost(models.Model):
    _inherit = 'blog.post'
    
    def action_post_debug_view(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').read()[0]

        action['views'] = [(self.env.ref('website_blog.view_blog_post_form').id, 'form')]
        action['res_id'] = self.id
        return action

    def action_post_code_view(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').read()[0]
    
        action['views'] = [(self.env.ref('app_website_blog_editor.app_blog_post_form_view_code').id, 'form')]
        action['res_id'] = self.id
        return action

