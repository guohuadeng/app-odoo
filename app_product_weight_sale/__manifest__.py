# -*- coding: utf-8 ---*---

{
    'name': 'Weight in Sales Order',
    'version': '12.19.06.10',
    'summary': 'Add Product sku weight in Sale Order, product weight, sale weight, sale order weight, total weight, kg kg(s) lb lb(s) support',
    'sequence': 10,
    'license': 'LGPL-3',
    'description': """
    All in one Weight solution for sale, purchase, purchase agreement, mrp, stock.
    Add product sku weight in Sale Order. Unit of measure auto weight, kg kg(s) lb lb(s) support. weight sale order.
    Calculates total weight of a sale order, which is the sum of individual weights of each unit of the products in the order。
    Support kg(s) or lb(s)
    """,
    'category': 'Sales',
    'author': 'odooai.cn',
    'website': 'https://www.odooai.cn',
    'images': ['static/description/banner.png'],
    'currency': 'EUR',
    'price': 38,
    'depends': ['sale_management'],
    'data': [
        'security/res_group.xml',
        'views/sale_config_settings_views.xml',
        'views/sale_order_views.xml',
        'report/report_sale_order_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
