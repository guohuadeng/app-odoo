# -*- coding: utf-8 -*-

# Created on 2023-10-23
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': "HR部门树形组件 / HR Department zTree Widget",
    'version': '18.0.24.12.09',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': 'HR部门员工父子树形选择器，zTree组件。/ HR department and employee parent children tree selector with zTree widget.',
    'description': """
English Features:
1. zTree widget for HR department and employee parent children tree navigation.
2. Advance search with real parent children tree in ListView or KanbanView.
3. Easy to use in product category, stock location, HR department.
4. Widget-based design, can be used anywhere in Odoo.
5. Multi-language Support. Multi-Company Support.
6. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
7. Full Open Source.

中文功能：
1. HR部门和员工父子树形导航zTree组件。
2. 支持在列表视图和看板视图中使用真实父子树形结构搜索。
3. 可用于产品分类、库存位置、HR部门等多种场景。
4. 基于组件设计，可在Odoo任何地方使用。
5. 多语言支持。多公司支持。
6. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
7. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'hr',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/hr_views.xml',
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
