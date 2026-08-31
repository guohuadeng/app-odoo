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
    'name': "POS销售单导航 / POS Order Navigator by Store",
    'version': '19.0.25.06.10',
    'author': 'odooai.cn',
    'category': 'Point of Sale',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': '按门店、销售员和状态浏览POS订单，Superbar高级搜索。/ Browse POS orders by store, salesperson and status with Superbar.',
    'description': """
English Features:
1. Superbar and zTree widget for POS order advance search.
2. Browse POS orders by store, salesperson and order status.
3. Advance search sidebar for many2one, many2many, date range, boolean, selection, number fields.
4. Search sidebar available for list, kanban, pivot and graph views.
5. Multi-language Support. Multi-Company Support.
6. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
7. Full Open Source.

中文功能：
1. POS订单Superbar和zTree高级搜索组件。
2. 按门店、销售员和订单状态浏览POS订单。
3. 高级搜索侧栏，支持many2one、many2many、日期范围、布尔、选择、数字字段。
4. 搜索侧栏支持列表、看板、数据透视和图表视图。
5. 多语言支持。多公司支持。
6. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
7. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'point_of_sale',
        'app_product_superbar',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/product_views.xml',
        'views/pos_order_views.xml',
        'views/report_pos_order_views.xml',
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
