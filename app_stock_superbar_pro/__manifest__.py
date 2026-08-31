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
    'name': '库存高级超级搜索栏 / Stock Superbar Pro with Date Search',
    'version': '19.0.25.09.08',
    'author': 'odooai.cn',
    'category': 'Inventory/Inventory',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '库存高级搜索，支持日期搜索和父子树导航 / Advance stock search with date range and parent children tree',
    'description': """
1. Pro version of Stock Superbar with advanced date search capabilities.
2. Support instant mode for one-click search and lazy mode for big data performance.
3. Advance search with real parent children tree in ListView, KanbanView, Pivot and Graph view.
4. Support stock picking, stock picking batch, stock move and stock move line views.
5. Support date range search for stock operations.
6. Easy to customize for any Odoo module with simple XML configuration.
7. Multi-Language Support.
8. Multi-Company Support.
9. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
10. Full Open Source under LGPL-3 license.
1. 库存超级搜索栏专业版，提供高级日期搜索功能。
2. 支持即时模式一键搜索，延迟模式适合大数据量性能优化。
3. 使用父子树结构在列表、看板、透视和图表视图中进行高级搜索。
4. 支持调拨单、批次调拨、库存移动和移动线视图。
5. 支持库存操作的日期范围搜索。
6. 通过简单 XML 配置即可在任何 Odoo 模块中定制使用。
7. 多语言支持。
8. 多公司支持。
9. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
10. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_stock_superbar',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/stock_picking_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_move_views.xml',
        'views/stock_move_line_views.xml',
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
