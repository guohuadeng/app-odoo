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
    'name': "活动高级搜索 / Event Advance Search Browse by Stage and Date",
    'version': '18.0.24.12.04',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按阶段和日期浏览活动，Superbar高级搜索侧栏。/ Browse event by stage and date with Superbar advance search sidebar.',
    'description': """
English Features:
1. Superbar and zTree widget for Event module advance search.
2. Advance search with real parent children tree, ListView or KanbanView.
3. Support parent tree, children tree navigation (e.g., event stage tree).
4. Quick advance search and navigator for all app data in tree list header.
5. Advance search sidebar for many2one, many2many, date range, datetime, boolean, selection, number fields.
6. Search sidebar available for list, kanban, pivot and graph views.
7. Support navigate in search more windows for m2o or m2m fields.
8. Easy customize for any app with extra param for searchpanel.
9. Multi-language Support. Multi-Company Support.
10. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
11. Full Open Source.

中文功能：
1. Event模块Superbar和zTree高级搜索组件。
2. 支持真实父子树形结构的高级搜索，列表视图和看板视图。
3. 支持父级树、子级树导航浏览（如活动阶段树）。
4. 树形列表头部快速高级搜索和数据导航。
5. 高级搜索侧栏，支持many2one、many2many、日期范围、日期时间、布尔、选择、数字字段。
6. 搜索侧栏支持列表、看板、数据透视和图表视图。
7. 支持在搜索更多窗口中为m2o/m2m字段导航筛选。
8. 易于自定义，支持searchpanel额外参数。
9. 多语言支持。多公司支持。
10. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
11. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'event',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/event_event_views.xml',
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
