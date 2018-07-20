# -*- coding: utf-8 ---*---
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'App Sales Order Weight',
    'version' : '11.1.6.17',
    'summary': 'Add sku weight in Sale Order',
    'sequence': 10,
    'license':'LGPL-3',
    'description': """
    Add sku weight in Sale Order.
    Calculates total weight of a sale order, which is the sum of individual weights of each unit of the products in the order
    """,
    'category': 'Sales',
    'author' : 'Sunpop.cn',
    'website' : 'http://www.sunpop.cn',
    'images': ['static/description/banner.jpg'],
    'depends' : ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
