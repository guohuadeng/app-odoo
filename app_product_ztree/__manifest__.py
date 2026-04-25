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
    'name': "产品分类树形组件 / Product Category zTree Widget",
    'version': '18.0.24.12.09',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '产品分类父子树形选择器，zTree组件。/ Product category parent children tree selector with zTree widget.',
    'description': """
English Features:
1. zTree widget for product category parent children tree navigation.
2. Advance search with real parent children tree in ListView or KanbanView.
3. Widget-based design, can be used anywhere in Odoo.
4. Multi-language Support. Multi-Company Support.
5. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
6. Full Open Source.

中文功能：
1. 产品分类父子树形导航zTree组件。
2. 支持在列表视图和看板视图中使用真实父子树形结构搜索。
3. 基于组件设计，可在Odoo任何地方使用。
4. 多语言支持。多公司支持。
5. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
6. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'product',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/product_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    # 'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
