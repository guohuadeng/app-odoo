# Copyright 2013-2015 Camptocamp SA - Nicolas Bessi
# Copyright 2013-2015 Camptocamp SA - Guewen Baconnier
# Copyright 2013-2015 Camptocamp SA - Yannick Vaucher
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Created on 2018-08-15
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': 'App Split Stock Picking',
    'summary': 'Split a picking in two not transferred pickings. Base on OCA',
    'version': '11.0.1.0.0',
    'category': 'Inventory',
    'author': "Sunpop.cn",
    'license': 'AGPL-3',
    'website': 'http://www.sunpop.cn',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_partial_picking.xml',
    ],
}
