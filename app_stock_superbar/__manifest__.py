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
    'name': '库存超级搜索栏 / Stock Superbar zTree Navigator',
    'version': '19.0.25.09.08',
    'author': 'odooai.cn',
    'category': 'Inventory/Inventory',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按库存位置和类型树状导航，支持调拨单、批次、移动线 / Stock location tree navigator for picking, batch, move and lot',
    'description': """
1. Stock Superbar with zTree widget for parent children tree navigation.
2. Advance search with real parent children tree in ListView, KanbanView, Pivot and Graph view.
3. Support stock location, stock picking, stock picking batch, stock picking type views.
4. Support stock warehouse orderpoint, stock rule, stock lot, stock move and move line views.
5. Easy to customize, you can use it anywhere in Odoo.
6. Multi-Language Support.
7. Multi-Company Support.
8. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
9. Full Open Source under LGPL-3 license.
1. 库存超级搜索栏（Superbar），使用 zTree 控件实现父子树导航。
2. 使用父子树结构在列表、看板、透视和图表视图中进行高级搜索。
3. 支持库存位置、调拨单、批次调拨、调拨类型视图。
4. 支持补货规则、库存批次、库存移动和移动线视图。
5. 易于定制，可在 Odoo 任何模块中使用。
6. 多语言支持。
7. 多公司支持。
8. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
9. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
        'stock_picking_batch',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_type_views.xml',
        'views/stock_warehouse_orderpoint_views.xml',
        'views/stock_rule_views.xml',
        'views/stock_lot_views.xml',
        'views/stock_move_line_views.xml',
        'views/stock_move_views.xml',
        # todo: 以下两个模型调整了
        # 'views/stock_location_route_views.xml',
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
