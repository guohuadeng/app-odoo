
{
    'name': 'App Customize Columns of List (Tree) View Dynamic',
    'version': '10.0.1.6',
    'author': '广州欧度智能',
    'category': 'Productivity',
    'website': 'http://www.odooapp.cn',
    'sequence': 2,
    'summary': 'App Customize columns of  List (Tree) View. Dynamic list.',
    'description': """

App Customize Columns of List (Tree) View
============
App Customize Columns of List (Tree) View module is made to show/hide the columns on the list/tree view of Odoo. After installing the module, a "Set Columns" button will be show to the list view.
You can customize every odoo list/tree view easily.

This module is ready for Community and Enterprise Edition.

    """,
    'images': ['static/description/sales_com.png'
    ],
    'depends': ['web'],
    'data': [
    'views/listview_button.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/listview_button_view.xml'],
}

