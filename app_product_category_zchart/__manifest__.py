# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/


{
    'name': "产品目录层级图 / Category zChart Hierarchy",
    'version': '19.0.25.02.27',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '产品目录多层级结构图组件，支持N+1/N+2级展示。/ Product category multi level hierarchy chart widget with N+1/N+2 support.',
    'description': """
English Features:
1. Hierarchy chart widget for product category multi level visualization.
2. Support N+1, N+2 direct subordinates in chart.
3. Free for category, stock and account hierarchy chart.
4. Multi-language Support. Multi-Company Support.
5. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
6. Full Open Source.

中文功能：
1. 产品目录多层级结构图组件。
2. 支持N+1、N+2级直接下属展示。
3. 免费用于产品分类、库存位置和会计科目层级图。
4. 多语言支持。多公司支持。
5. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
6. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'product',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/product_category_views.xml',
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
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
