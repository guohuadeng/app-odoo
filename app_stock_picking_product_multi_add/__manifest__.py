# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': '库存调拨单批量添加产品 / Stock Picking Order Product Multi Batch Add',
    'version': '18.0.24.12.03',
    'author': 'odooai.cn',
    'category': 'Inventory/Inventory',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': '一键批量将多个产品添加到库存调拨单 / One-click to add multi products to stock picking order',
    'description': """
1. One-click to add multi products to Stock Picking Order.
2. All products can be filtered and grouped before adding.
3. Support sale order, purchase order, MRP BOM and account invoice multi-add.
4. You can make any one2many field to get this feature by configuring the XML.
5. Multi-Language Support.
6. Multi-Company Support.
7. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
8. Full Open Source under LGPL-3 license.
1. 一键快速将多个产品添加到库存调拨单中。
2. 可对产品进行过滤、分组，然后批量加入调拨单。
3. 支持销售订单、采购订单、MRP BOM 和会计发票的多行添加。
4. 通过 XML 配置可为任何 one2many 字段启用此功能。
5. 多语言支持。
6. 多公司支持。
7. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
8. 代码完全开源，基于 LGPL-3 协议。
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'stock',
    ],
    'images': ['static/description/stock1.gif'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
