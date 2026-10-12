# -*- coding: utf-8 -*-

# Created on 2017-11-28
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_document_offline/
# description:
# v20: 原 show_short_category 短名需求已由原生 _compute_display_name 的
# hierarchical_naming 上下文承接（hierarchical_naming=False 时 display_name 取短名 name），
# 本文件保留类壳供后续扩展，暂不加载（见 __init__.py）。

from odoo import models


class ProductCategory(models.Model):
    _inherit = 'product.category'
