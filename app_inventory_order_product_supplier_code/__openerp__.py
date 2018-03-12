# -*- coding: utf-8 -*-

# Created on 2018-03-12
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

{
    "name": "App Inventory Order with Product Supplier Code",
    "summary": "This module adds the supplier code defined in the product, to the Inventory Order line.",
    "version": "10.0.1",
    "author": "Sunpop.cn",
    "website": "http://www.sunpop.cn",
    "category": "Warehouse",
    "depends": ["purchase"],
    "license": "AGPL-3",
    'sequence': 3,
    "data": [
        "views/stock_picking_views.xml",
        "views/stock_move_views.xml",
    ],
    'images': ['static/description/set1.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
    "price": 68.00,
    "currency": "EUR",
    'description': """

==============================
App Inventory Order Product Supplier Code
==============================
This module adds the supplier code defined in the product, to the Inventory Order line.

Usage
=====

To use this module:

#. Go to 'Inventory' and open a Inventory Order.
#. If the vendor has defined some code for any Inventory Order line they will be
   displayed in the line under the column 'Product Supplier Code'.
   """,
}
