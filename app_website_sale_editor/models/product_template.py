# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def action_product_code_view(self):
        self.ensure_one()
        
        action = self.env.ref('website_sale.action_product_pages_list').read()[0]

        action['views'] = [(self.env.ref('app_website_sale_editor.product_template_form_view_src').id, 'form')]
        action['res_id'] = self.id
        return action

