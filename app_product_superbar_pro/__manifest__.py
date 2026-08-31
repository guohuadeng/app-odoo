# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': "产品分类导航Pro版 / Product Browse by Category Navigator Pro",
    'version': '19.0.25.04.19',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '产品分类高级搜索Pro增强版，更多功能特性。/ Product category advance search Pro version with enhanced features.',
    'description': """
English Features:
1. Superbar and zTree widget for product advance search (Pro enhanced version).
2. Browse products by category tree with real parent children hierarchy.
3. Advance search sidebar for many2one, many2many, date range, boolean, selection, number fields.
4. Search sidebar available for list, kanban, pivot and graph views.
5. Pro features for enhanced product browsing experience.
6. Multi-language Support. Multi-Company Support.
7. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
8. Full Open Source.

中文功能：
1. 产品Superbar和zTree高级搜索Pro增强版组件。
2. 按分类树形浏览产品，支持真实父子层级关系。
3. 高级搜索侧栏，支持多种字段类型。
4. Pro增强功能，提升产品浏览体验。
5. 多语言支持。多公司支持。
6. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
7. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_product_superbar',
    ],
    'images': ['static/description/superbar_pro.gif', 'static/description/banner.png'],
    'data': [
        'views/product_views.xml',
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
