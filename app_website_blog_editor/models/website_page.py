# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WebsitePage(models.Model):
    _inherit = 'website.page'

    is_force_all = fields.Boolean('Force All Website', default=False,
                                  help='If check, the page would use to all website, even u change.')

    def write(self, vals):
        # 处理强制全局, Create时不管
        for page in self:
            if page.is_force_all or vals.get('is_force_all'):
                vals.update({
                    'website_id': False
                })
        return super(WebsitePage, self).write(vals)

    def action_page_debug_view(self):
        # 直接覆盖原生
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ir.ui.view',
            'res_id': self.view_id.id,
            'view_mode': 'form',
            'view_id': self.env.ref('app_website_blog_editor.app_view_view_form_extend_debug').id,
        }

    def action_page_code_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ir.ui.view',
            'res_id': self.view_id.id,
            'view_mode': 'form',
            'view_id': self.env.ref('website.view_view_form_extend').id,
        }

    def action_page_form_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'website.page',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('website.website_pages_form_view').id,
        }
