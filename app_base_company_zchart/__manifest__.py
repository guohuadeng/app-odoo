# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2026 odooAi.cn

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# 行业应用说明，应该是带 Industry 的就会放入

##############################################################################
#    Copyright (C) 2009-TODAY odooAi.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "集团公司多层级结构图,Group Company Multi Level Chart Hierarchy",
    'version': '19.0.25.06.10',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': "集团公司多层级树状结构图，zChart widget。Multi level company hierarchy chart with zChart widget for parent-children relation.",
    'description': '''
    1. Group Company Chart Hierarchy with zChart widget for multi level parent-children relation tree.
    2. Visualize company structure hierarchy with interactive chart.
    3. Support force set parent company wizard for batch updates.
    4. Multi-language Support. Multi-Company Support.
    5. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    6. Full Open Source.

    1. 集团公司多层级树状结构图，zChart widget
    2. 可视化展示公司层级结构
    3. 支持批量设置上级公司的向导
    4. 多语言支持，多公司支持
    5. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    6. 代码完全开源
    ''',
    'depends': [
        'app_common',
        # 'website',
    ],
    'data': [
        'security/res_group.xml',
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'wizard/force_set_parent_company_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'app_/static/src/scss/style.scss',
        ],
        'web.assets_backend': [
            # 'app_/static/src/js/*.js',
        ],
    },
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
