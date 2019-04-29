# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': "App stock picking browse by type",
    'version': '12.19.04.12',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    stock picking filter by picking type. Use for parent children  kanban navigator. 
    dynanmic kanban. Hierarchy Tree. Parent Children relation tree filter, navigator.
    """,
    'description': """
    Feature of odoo13. Support one2many field and kanban view.
    Advance Search, Advance Filter with Parent Children Tree.
    Easy to navigator and browse any data.
    Ready for any odoo module. Like product, partner, sales order, purchase order, account, stock.
    easy use, like:    
    <searchpanel>
        <field name='partner_id'/>
    </searchpanel>
    The limit of the apps is only support many2one field and kanban view. also not good for domain filter of panel.
    If you want more powerful function. please go to https://www.odoo.com/apps/modules/12.0/app_web_superbar
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/stock_location_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
