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
    'name': "采购超级搜索导航 / Purchase Superbar Navigator",
    'version': '19.0.26.08.19',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '采购订单按供应商树状导航，支持列表、看板、透视表、图表视图 / Browse purchase orders by vendor with tree navigator across list, kanban, pivot and graph views.',
    'description': """
1. Purchase order search panel with partner/vendor tree navigation
2. Purchase order search panel with state and invoice status filtering
3. Purchase request quotation search panel with partner tree navigation
4. Product supplier info search panel with partner and product tree navigation
5. Multi-company support with company-based filtering in search panels
6. Enhanced purchase report with search panel navigation
7. Support for list view, kanban view, pivot view and graph view in superbar
8. Multi-select nodes with Ctrl/Cmd key for advanced filtering
9. Real parent-children tree structure navigation
10. Easy to customize, reusable search panel widget for any Odoo model
11. Multi-language support for global enterprise deployment
12. Full version support (Odoo 19, 18, 17, 16, 15, 14, 13, 12)
13. Full open source under LGPL-3 license

1. 采购订单按供应商树状导航搜索
2. 采购订单按状态和开票状态过滤
3. 采购询价单按供应商树状导航搜索
4. 产品供应商信息按供应商和产品树状导航搜索
5. 多公司支持，搜索面板按公司过滤
6. 采购报表增强搜索面板导航
7. 支持列表、看板、透视表、图表视图中的超级搜索栏
8. Ctrl/Cmd 键多选节点高级过滤
9. 真实的父子树状结构导航
10. 易于定制，可在任意 Odoo 模型中复用搜索面板
11. 多语言支持，适配全球化企业部署
12. 全版本支持（Odoo 19, 18, 17, 16, 15, 14, 13, 12）
13. 代码完全开源，基于 LGPL-3 协议
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'purchase',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/purchase_order_views.xml',
        'views/product_supplierinfo_views.xml',
        'report/purchase_report_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'app_purchase_superbar/static/src/views/*.xml',
            'app_purchase_superbar/static/src/scss/app_style_after.scss',
        ],
    },
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
