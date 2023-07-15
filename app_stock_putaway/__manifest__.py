# -*- coding: utf-8 -*-

# Created on 2018-11-05
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:


{
    'name': "App stock putaway show.单独的上架策略界面及菜单",
    'version': '12.0.11.14',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Show stock putaway strategy in stock menu.
    """,
    'description': """
    上架策略菜单。
    每个上架策略只适用于指定位置
    欧度智能，odooai.cn 的odoo模块。
    """,
    'depends': ['stock'],
    'images': [],

    'data': [
        'views/stock_location_views.xml',
        'views/product_putaway_views.xml',
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
