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
    'name': '销售订单高级超级搜索栏 / Advance Sale Order Navigator by Partner and Channel',
    'version': '19.0.24.12.04',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按客户和销售渠道高级浏览销售订单，即时和延迟搜索模式 / Advance browse sale orders by partner and channel with instant and lazy search mode',
    'description': """
1. Pro version of Sale Order Superbar with advanced search capabilities.
2. Support instant mode for one-click search and lazy mode for big data performance.
3. Advance search with real parent children tree in ListView, KanbanView, Pivot and Graph view.
4. Support search more view for quick product lookup.
5. Support multi-field search and filter.
6. Mobile responsive view, optimized for big screen HD view.
7. Easy to customize for any Odoo module with simple XML configuration.
8. Multi-Language Support.
9. Multi-Company Support.
10. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
11. Full Open Source under LGPL-3 license.
1. 销售订单超级搜索栏专业版，提供高级搜索功能。
2. 支持即时模式一键搜索，延迟模式适合大数据量性能优化。
3. 使用父子树结构在列表、看板、透视和图表视图中进行高级搜索。
4. 支持搜索更多视图，快速查找产品。
5. 支持多字段搜索和筛选。
6. 移动端自适应响应式视图，优化大屏幕高清显示。
7. 通过简单 XML 配置即可在任何 Odoo 模块中定制使用。
8. 多语言支持。
9. 多公司支持。
10. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
11. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_sale_superbar',
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
