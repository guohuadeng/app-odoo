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
    'name': "采购订单高级搜索Pro / Purchase Order Navigator Pro",
    'version': '18.0.24.12.04',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按日期和供应商浏览采购订单，Superbar Pro高级搜索。/ Browse purchase orders by date and vendor with Superbar Pro.',
    'description': """
English Features:
1. Superbar Pro for purchase order advance search.
2. Browse purchase orders by date, partner vendor and status.
3. Advance search sidebar for multiple field types.
4. Search sidebar available for list, kanban, pivot and graph views.
5. Pro features for enhanced purchase browsing experience.
6. Multi-language Support. Multi-Company Support.
7. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
8. Full Open Source.

中文功能：
1. 采购订单Superbar Pro高级搜索组件。
2. 按日期、供应商和状态浏览采购订单。
3. 高级搜索侧栏，支持多种字段类型。
4. Pro增强功能，提升采购浏览体验。
5. 多语言支持。多公司支持。
6. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
7. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_purchase_superbar',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/purchase_order_views.xml',
        'report/purchase_report_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
