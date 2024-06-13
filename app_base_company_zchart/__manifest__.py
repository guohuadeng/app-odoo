# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2023 odooAi.cn

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
    'name': 'Group Company Multi Level Chart Hierarchy, 集团公司多层级结构图zChart',
    'version': '16.24.05.06',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 999.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Group Company Chart Hierarchy with zchart Widget. Hierarchy Chart, Hierarchy Tree for multi level Parent Children relation tree.
    Free for Multi company Hierarchy chart category Hierarchy chart, stock Hierarchy chart. account chart. user multi level chart.
    ''',
    'description': '''
Need extra paid apps https://www.odoo.com/apps/modules/16.0/app_web_widget_ztree/
This module extend to show a Hierarchy chart
    1. app of odooapp.cn
    2.
    3.
    4.
    5.
    6.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ========== 中文说明
    1.
    2.
    3.
    4.
    11. 多语言支持，多公司支持
    12. Odoo 17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
    ''',
    'depends': [
        'app_common',
        # 'website',
    ],
    'data': [
        'security/res_group.xml',
        'views/res_company_views.xml',
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
