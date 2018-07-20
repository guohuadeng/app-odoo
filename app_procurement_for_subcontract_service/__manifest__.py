# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# base on Camptocamp, Odoo Community Association (OCA)

{
    "name": 'App procurement for Subcontracted service',
    "version": "11.0.1.0.0",
    "category": "Purchase",
    "website": "http://www.sunpop.cn/",
    "author": "Sunpop.cn",
    "license": "AGPL-3",
    'sequence': 3,
    "summary": 'procurement for  Subcontracted service(委外采购), Subcontracted base module',
    'description': """
    """,
    'price': 68.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
    "depends": [
        "purchase",
    ],
    "data": [
        'views/product_template.xml',
        'views/warehouse.xml',
    ],
    "post_init_hook": "post_init_hook",
}
