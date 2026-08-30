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
    'name': "MRP制造单导航 / MRP Manufacturing Orders Navigator",
    'version': '19.0.25.06.10',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按物料可用性和工作中心浏览制造单，Superbar高级搜索。/ Browse manufacturing orders by materials availability and work center with Superbar.',
    'description': """
English Features:
1. Superbar and zTree widget for MRP manufacturing orders advance search.
2. Browse manufacturing orders by state, work center and materials availability.
3. Advance search sidebar for many2one, many2many, date range, boolean, selection, number fields.
4. Search sidebar available for list, kanban, pivot and graph views.
5. Support navigate in search more windows for m2o or m2m fields.
6. Easy customize for any app with extra param for searchpanel.
7. Multi-language Support. Multi-Company Support.
8. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
9. Full Open Source.

中文功能：
1. MRP制造单Superbar和zTree高级搜索组件。
2. 按状态、工作中心和物料可用性浏览制造单。
3. 高级搜索侧栏，支持many2one、many2many、日期范围、布尔、选择、数字字段。
4. 搜索侧栏支持列表、看板、数据透视和图表视图。
5. 支持在搜索更多窗口中为m2o/m2m字段导航筛选。
6. 易于自定义，支持searchpanel额外参数。
7. 多语言支持。多公司支持。
8. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
9. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'mrp',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        # 'data/ir_data.xml',
        'views/mrp_production_views.xml',
        'views/mrp_workorder_views.xml',
        'views/mrp_bom_views.xml',
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
