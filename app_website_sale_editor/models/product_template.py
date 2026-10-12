# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.tools.safe_eval import safe_eval


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_product_debug_view(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id('website_sale.product_template_action_website')

        action['views'] = [(self.env.ref('app_website_sale_editor.app_product_template_form_view_debug').id, 'form')]
        action['res_id'] = self.id
        return action

    def action_product_code_view(self):
        self.ensure_one()

        # v20 断点：website_sale 的「产品页面」一套数据文件（v18 website_sale/views/
        # website_pages_views.xml:4/:72 的 product_pages_tree_view 与 action_product_pages_list）
        # 在 v20 已整体删除，电商产品列表/动作换成 product_template_view_tree_website_sale 与
        # product_template_action_website ⇒ 这里改用后者（与上面 action_product_debug_view 一致）。
        action = self.env["ir.actions.actions"]._for_xml_id('website_sale.product_template_action_website')

        action['views'] = [(self.env.ref('app_website_sale_editor.app_product_template_form_view_code').id, 'form')]
        action['res_id'] = self.id
        return action

