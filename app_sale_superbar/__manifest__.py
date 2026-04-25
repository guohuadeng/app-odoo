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
    'name': '销售订单超级搜索栏 / App Sale Order Browse by Partner and Channel',
    'version': '18.0.25.06.10',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按客户和销售渠道浏览销售订单，树状层级导航 / Browse sale order by partner and sale channel with parent children tree navigator',
    'description': """
1. Browse sale orders by partner and sale channel with parent children tree navigator.
2. Advance search with real parent children tree in ListView, KanbanView, Pivot and Graph view.
3. Support search more view for quick product lookup.
4. Easy to customize, you can use it anywhere in Odoo.
5. Multi-Language Support.
6. Multi-Company Support.
7. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
8. Full Open Source under LGPL-3 license.
1. 按客户和销售渠道浏览销售订单，支持树状层级导航。
2. 使用父子树结构在列表、看板、数据透视和图表视图中进行高级搜索。
3. 支持搜索更多视图，快速查找产品。
4. 易于定制，可在 Odoo 任何模块中使用。
5. 多语言支持。
6. 多公司支持。
7. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
8. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'sale_management',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/sale_order_views.xml',
        'report/sale_report_views.xml',
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
