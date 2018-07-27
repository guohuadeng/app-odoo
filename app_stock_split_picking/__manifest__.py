# Copyright 2013-2015 Camptocamp SA - Nicolas Bessi
# Copyright 2013-2015 Camptocamp SA - Guewen Baconnier
# Copyright 2013-2015 Camptocamp SA - Yannick Vaucher
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'App Split picking',
    'summary': 'Split a picking in two not transferred pickings',
    'version': '11.0.1.0.0',
    'category': 'Inventory',
    'author': "Camptocamp, "
              "Tecnativa, "
              "Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/stock-logistics-workflow',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_partial_picking.xml',
    ],
}
