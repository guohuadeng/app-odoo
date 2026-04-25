# -*- coding: utf-8 -*-

# Created on 2023-10-20
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2026 odooAi.cn

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
    'name': "客户发票与供应商账单批量添加产品,Account Invoice Product Multi Add",
    'version': '18.0.24.12.03',
    'author': 'odooai.cn',
    'category': 'Accounting/Accounting',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': "一键批量将多个产品添加到客户发票与供应商账单中，支持过滤与分组。One Click to batch add multiple products to Customer Invoice and Vendor Bill with filter and group.",
    'description': """
    1. One Click to add multi product to Account Customer Invoice and Vendor Bill.
    2. All the products can be filtered and grouped by category in the popup window.
    3. Multi select products and batch add to invoice lines.
    4. Supports any one2many field to get this feature by XML configuration.
    5. Also works with Sale Order, Purchase Order, MRP BOM, and Stock Picking.
    6. Multi-language Support. Multi-Company Support.
    7. Support Odoo 18, 17, 16, 15, 14, 13, 12, Enterprise and Community and odoo.sh Edition.
    8. Full Open Source.

    1. 一键快速将多个产品批量添加到客户收据与供应商账单中
    2. 可在弹窗中对产品进行过滤、分组，然后批量加入发票行
    3. 支持多选产品，一次性添加到账单明细
    4. 可通过XML配置让任意one2many字段获得此功能
    5. 同样适用于销售订单、采购订单、MRP BOM和库存拣货
    6. 多语言支持，多公司支持
    7. Odoo 18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    8. 代码完全开源
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
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
