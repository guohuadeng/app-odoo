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
    'name': "会计科目树状导航,Account Superbar Navigator",
    'version': '19.0.26.08.21',
    'author': 'odooai.cn',
    'category': 'Accounting/Accounting',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': "会计科目树状导航，按科目表结构浏览日记账、凭证行、辅助核算。Browse journal by account chart with parent-children tree navigator for list, kanban, pivot, graph view.",
    'description': """
    1. Advance search with real parent-children tree navigator for Account Chart views.
    2. Browse Account Account, Analytic Account, Journal Items, Journal Entries, Analytic Lines by tree structure.
    3. Support tree view, list view, kanban view, pivot view and graph view.
    4. Click to expand/collapse tree nodes, Ctrl/Cmd to multi-select nodes.
    5. Set checkbox to include or exclude child nodes data.
    6. Multi-field search and filter support.
    7. Multi-language Support. Multi-Company Support.
    8. Support Odoo 18, 17, 16, 15, 14, 13, 12, Enterprise and Community and odoo.sh Edition.
    9. Full Open Source.

    1. 会计科目树状高级导航，支持科目、辅助核算、凭证、凭证行、辅助核算分录
    2. 按科目表父子结构浏览会计数据
    3. 支持树形、列表、看板、透视表、图表等多种视图
    4. 点击展开/折叠树节点，Ctrl/Cmd多选节点
    5. 勾选控制是否包含子节点数据
    6. 支持多字段搜索与过滤
    7. 多语言支持，多公司支持
    8. Odoo 18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    9. 代码完全开源
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'account',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
        'views/account_analytic_account_views.xml',
        'views/account_move_line_views.xml',
        'views/account_move_views.xml',
        'views/account_analytic_line_views.xml',
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
