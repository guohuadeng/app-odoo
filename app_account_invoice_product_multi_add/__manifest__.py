# -*- coding: utf-8 -*-

# Created on 2023-10-20
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2024 odooAi.cn

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

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
    'name': "App Account Invoice Product Multi Batch Add",
    'version': '24.03.21',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': """
    App Account Invoice Product Multi Batch Add
    Odoo App of odooai.cn
    """,
    'description': """
    App Account Invoice Product Multi Add
    1. One Click to add multi product to Account Invoice.
    2. All the product can filter and group.
    客户收据与供应商帐单批量增加产品
    1. 可以一键快速将多个产品加到客户收据与供应商帐单中
    2. 可对产品进行过滤、分组，然后批量加入
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'account',
    ],
    'images': ['static/description/account1.gif'],
    'data': [
        'views/account_move_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
