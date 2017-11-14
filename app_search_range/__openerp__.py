# -*- coding: utf-8 -*-
{
    'name': 'App Search By Date or Number Range',
    'version': '10.0.1.0',
    'author': 'Sunpop.cn',
    'category': 'web',
    'website': 'http://www.sunpop.cn',
    'sequence': 2,
    'summary': 'Search by date or number range in List view and Pivot view',
    'description': """

Search by date or number range in List view and Pivot view
--------------------------------------------------

    """,
    'depends': ['web'],
    'data': [
        'views/template_view.xml',
        # data
        'data/ir_config_parameter.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    "price": 0.00,
    "currency": "EUR",
    
    'images': ['static/description/list_pivot.png'],

    'installable': True,
    'auto_install': False,
    'application': False,
}
