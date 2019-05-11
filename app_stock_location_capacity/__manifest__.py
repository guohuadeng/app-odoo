# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# http://www.sunpop.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/


{
    'name': "Capacity of Stock Location，货架容量管理",
    'version': '12.19.03.18',
    'author': 'Sunpop.cn',
    'category': 'Warehouse',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Add stock shelf, stock rack, stock slot manager. Shelf Auto Name with XYZ like WH-X1-Y2-Z6.
    Add shelf menu.
    """,
    'description': """    
    
    1. 
    """,
    'price': 68.00,
    'currency': 'EUR',
    'depends': [
        'stock',
        'app_stock_location_kanban',
    ],
    'images': ['static/description/banner.png'],
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
    ],
    'js': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
