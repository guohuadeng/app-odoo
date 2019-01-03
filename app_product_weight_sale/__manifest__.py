# -*- coding: utf-8 ---*---
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'App Product Weight in Sales Order',
    'version': '12.19.01.03',
    'summary': 'Add Product sku weight in Sale Order, product weight, sale weight, sale order weight, total weight, kg kg(s) lb lb(s) support',
    'sequence': 10,
    'license': 'LGPL-3',
    'description': """
    Add product sku weight in Sale Order. Unit of measure auto weight, kg kg(s) lb lb(s) support. weight sale order.
    Calculates total weight of a sale order, which is the sum of individual weights of each unit of the products in the order。
    Support kg(s) or lb(s)
    """,
    'category': 'Sales',
    'author': 'Sunpop.cn',
    'website': 'http://www.sunpop.cn',
    'images': ['static/description/banner.jpg'],
    'currency': 'EUR',
    'price': 38,
    'depends': ['sale_management'],
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
