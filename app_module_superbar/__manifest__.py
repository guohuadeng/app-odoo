# -*- coding: utf-8 -*-

# Created on 2023-10-23
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

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
    'name': "应用模块导航 / Apps Navigator by Category",
    'version': '19.0.24.11.12',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按分类树形浏览应用和模块。/ Browse apps by category tree and module navigator with Superbar.',
    'description': """
English Features:
1. Superbar widget for Apps and Module advance search by category tree.
2. Browse apps by category with real parent children hierarchy.
3. Module navigator for quick access to installed modules.
4. Advance search sidebar for multiple field types.
5. Search sidebar available for list, kanban, pivot and graph views.
6. Easy customize for any app with extra param for searchpanel.
7. Multi-language Support. Multi-Company Support.
8. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
9. Full Open Source.

中文功能：
1. 应用和模块Superbar高级搜索组件。
2. 按分类树形浏览应用，支持真实父子层级关系。
3. 模块导航器，快速访问已安装模块。
4. 高级搜索侧栏，支持多种字段类型。
5. 搜索侧栏支持列表、看板、数据透视和图表视图。
6. 易于自定义，支持searchpanel额外参数。
7. 多语言支持。多公司支持。
8. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
9. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'base',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/module_views.xml',
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
