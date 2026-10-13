# -*- coding: utf-8 -*-

# Created on 2017-11-28
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

from odoo import api, fields, models, exceptions, _

class ProductCategory(models.Model):
    _inherit = 'product.category'

    # 更新 display_name 算法，当 env.context: show_short =1 时，只显示短名
    # v18 的 name_get 覆写在 v20 已废弃，改为 _compute_display_name（v20 orm/models.py display_name 计算）
    @api.depends('name')
    def _compute_display_name(self):
        if self.env.context.get('show_short'):
            for category in self:
                category.display_name = category.name
        else:
            return super()._compute_display_name()
