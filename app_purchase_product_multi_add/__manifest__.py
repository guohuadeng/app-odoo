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
    'name': "采购订单批量添加产品 / Purchase Order Product Multi Batch Add",
    'version': '18.0.24.12.03',
    'author': 'odooai.cn',
    'category': 'Inventory/Purchase',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': '一键批量将多个产品添加到采购订单，支持过滤、分组和明细录入。/ One click batch add products to purchase order with filter, group and detail form.',
    'description': """
English Features:
1. One click to add multi products to purchase order.
2. All the products can be filtered and grouped before adding.
3. Pop a detail form to add purchase line with detail information.
4. Support both list-add and form-add modes.
5. Multi-language Support. Multi-Company Support.
6. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
7. Full Open Source.

中文功能：
1. 一键快速将多个产品加到采购订单中。
2. 可对产品进行过滤、分组，然后批量加入。
3. 可以弹出明细录入界面添加，便于同时支持列表添加及表单添加。
4. 多语言支持。多公司支持。
5. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
6. 代码完全开源。
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'purchase',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/purchase_order_views.xml',
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
