# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WebsitePage(models.Model):
    _inherit = 'website.page'

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
