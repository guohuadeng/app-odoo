# -*- coding: utf-8 -*-

# Created on 2018-08-15
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
    'name': 'Crm Advance search, Navigator by stage and team',
    'version': '16.23.09.01',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': """
    CRM Superbar.
    odoo Seo Advance Search, Advance Filter for Date search. date range search. Datetime search.
    M2M, selection, boolean, number search. Quick search in header.
    Support list, kanban, pivot, graph, search more view.
    """,
    'description': """
    Crm free app for app_web_superbar.
    Advance quick search for various field in all odoo app. Support list, kanban, pivot, graph, search more views.
    Search with Hierarchy Parent Children Tree. seo search.
    odoo高级搜索，日期搜索，时间搜索，字符串搜索，数字搜索，下拉搜索. 列表快速搜索。
    超级方便的查询，树状视图导航。可用在任何模块中。
    1. Quick Advance Search and navigator for all app data. 20+ free odoo app search in box.
    2. Quick search in tree list header. Date range, Datetime, selection, number supported.
    3. Advance search sidebar for many2one, many2many field. m2o search, m2m search for multi select.
    4. Advance sidebar for date range search, datetime search, boolean search, selection search, number search.
    5. Search sidebar for list, kanban.Add more pivot, graph views than origin odoo.
    6. Support navigate in search more. Quick filter and search for m2o or m2m field.
    7. Easy customize for any app. any module. Use extra param for searchpanel of odoo. Para: view_types, class, name_field, icon, groups, filter_domain
    8. Advance search in box: Product, CRM, Sales, Purchase, MRP, Stock, Accounting, HR, Project, Etc.
    Extra param for searchpanel. view_types, class, name_field, icon, groups, filter_domain.
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'crm',
        'utm',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
