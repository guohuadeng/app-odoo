# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': "MRP Bom批量添加产品 / MRP Bom Product Multi Batch Add",
    'version': '18.0.25.09.16',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': '一键批量将多个产品添加到制造BOM中，支持过滤和分组。/ One click to batch add multiple products to MRP BOM with filter and group.',
    'description': """
English Features:
1. One click to add multi products to MRP BOM.
2. All the products can be filtered and grouped before adding.
3. Support batch selection and quick addition.
4. Multi-language Support. Multi-Company Support.
5. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
6. Full Open Source.

中文功能：
1. 一键快速将多个产品加到制造BOM中。
2. 可对产品进行过滤、分组，然后批量加入。
3. 支持批量选择和快速添加。
4. 多语言支持。多公司支持。
5. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
6. 代码完全开源。
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'mrp',
    ],
    'images': ['static/description/mrp1.gif'],
    'data': [
        'views/mrp_bom_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
