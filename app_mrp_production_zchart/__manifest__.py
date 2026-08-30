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
    'name': "MRP生产单层级图 / MRP Production zChart Hierarchy",
    'version': '19.0.25.08.26',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': 'MRP制造单多层级结构图，支持N+1、N+2级直接下属展示。/ Multi level MO hierarchy chart for MRP production order with N+1/N+2 subordinates.',
    'description': """
English Features:
1. MRP Hierarchy chart for Manufacturing Orders (MO).
2. Multi level MO production order from multi BOM support.
3. Hierarchy Tree for multi level parent children relation.
4. Show N+1, N+2 direct subordinates in chart.
5. Chart Hierarchy Widget with image, description and children count fields.
6. Multi-language Support. Multi-Company Support.
7. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
8. Full Open Source.

中文功能：
1. MRP制造单层级图。
2. 支持多级BOM展开的多层级制造单。
3. 多层级父子关系层级树。
4. 图表中展示N+1、N+2级直接下属。
5. 层级图组件，支持图片、描述和子项计数字段。
6. 多语言支持。多公司支持。
7. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
8. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'mrp',
    ],
    # 不要误装别的，避免冲突
    'excludes': [
        'app_mrp_production_chart',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'demo': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
