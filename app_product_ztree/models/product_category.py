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

    # 更新 complete_name 算法，当有context: show_short_category =1 时，只显示短名
    # v20：原生 BaseModel 已删除 name_get()，显示名改由 _compute_display_name 承载
    #      （原生 product.category 自身就用这个钩子做 hierarchical_naming 长短名切换，
    #       见 odoo/addons/product/models/product_category.py:65-68）
    # 注意：本文件在 v18 起就未被 models/__init__.py 导入，属未装载代码；此处仅做 v20 API 对齐，
    #      不新增导入以免改变模块既有行为（详见升级报告）
    @api.depends_context('show_short_category')
    def _compute_display_name(self):
        if self.env.context.get('show_short_category'):
            for category in self:
                category.display_name = category.name
        else:
            return super(ProductCategory, self)._compute_display_name()
