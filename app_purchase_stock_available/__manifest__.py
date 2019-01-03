# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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
    "name": "Stock available in Purchase order line, Forecast",
    'summary': 'App Show product Quantity on hand and Forecast Quantity in Purchase Order',
    "version": "11.19.1.4",
    'category': 'Purchases',
    'author': 'Sunpop.cn',
    'website': 'http://www.sunpop.cn',
    'license': 'AGPL-3',
    'sequence': 2,
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/banner.png'],
    'currency': 'EUR',
    'price': 18,
    'description': """
        App Show stock product Quantity on hand and Forecast Quantity in Purchase Order
        采购单中显示产品库存量
    """,
    'depends': [
        'purchase',
        'stock',
    ],
    "data": [
        'views/purchase_order_views.xml',
    ],
    "installable": True
}
