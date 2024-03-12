# -*- coding: utf-8 -*-

import json
from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class BlogPost(models.Model):
    _inherit = 'blog.post'
    
    # 不允许暴力删除
    blog_id = fields.Many2one('blog.blog', ondelete='restrict')
    
    def write(self, vals):
        if vals.get('website_meta_og_img'):
            sync_blog_meta_background_img = self.env['ir.config_parameter'].sudo().get_param('app_website_blog_editor.sync_blog_meta_background_img')
            if sync_blog_meta_background_img:
                web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
                img_url = vals.get('website_meta_og_img').replace(web_base_url, '')
                for rec in self:
                    cover_properties = json.loads(rec.cover_properties)
                    cover_properties.update({
                        'background-image': 'url("%s")' % img_url,
                    })
                    vals.update({
                        'cover_properties': json.dumps(cover_properties)
                    })
        return super(BlogPost, self).write(vals)

    def action_post_debug_view(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').sudo().read()[0]

        action['views'] = [(self.env.ref('website_blog.view_blog_post_form').id, 'form')]
        action['res_id'] = self.id
        return action

    def action_post_code_view(self):
        self.ensure_one()
        action = self.env.ref('website_blog.action_blog_post').sudo().read()[0]
    
        action['views'] = [(self.env.ref('app_website_blog_editor.app_blog_post_form_view_code').id, 'form')]
        action['res_id'] = self.id
        return action
