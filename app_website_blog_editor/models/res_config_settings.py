# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sync_blog_meta_background_img = fields.Boolean('Use a meta image by default for blog post background', config_parameter='app_website_blog_editor.sync_blog_meta_background_img')

    def set_values(self):
        res = super().set_values()
        # v20：set_param 已删除，按值类型改 set_bool（字段是 Boolean）
        self.env['ir.config_parameter'].set_bool('app_website_blog_editor.sync_blog_meta_background_img', self.sync_blog_meta_background_img)
        return res
