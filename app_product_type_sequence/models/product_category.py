# -*- coding: utf-8 -*-

# Created on 2017-11-28
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

from openerp import api, fields, models, exceptions, _


class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = ['product.category']

    internal_type = fields.Many2one(
        'product.internal.type', 'Default Internal Type',
        auto_join=True, required=False)
