# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# base on Camptocamp, Odoo Community Association (OCA)

{
    "name": 'App Sale for Subcontracted service',
    "version": "11.0.1.0.0",
    "category": "Sale",
    "website": "http://www.sunpop.cn/",
    "author": "Sunpop.cn",
    "license": "AGPL-3",
    'sequence': 3,
    "summary": 'Sale for  Subcontracted service(委外采购的销售整合)',
    'description': """
    """,
    'price': 68.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
    "depends": [
        "app_procurement_for_subcontract_service",
        "sale_stock",
    ],
    "data": [
    ],
}
