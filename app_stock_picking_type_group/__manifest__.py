# -*- coding: utf-8 -*-

# Created on 2017-11-05
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
    'name': "App stock picking type group,库存作业类型分组",
    'version': '12.0.12.26',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Stock picking group in list or kanban view.
    """,
    'description': """
    模块开发模板，目录结构与文件定义。
    欧度智能，odooai.cn 的odoo模块。用于将库存作业分组，UI更方便。
    """,
    'depends': ['stock'],
    'images': ['static/description/demo1.jpg'],
    'currency': 'EUR',
    'price': 18,
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_type_group_views.xml',
        'views/stock_picking_type_views.xml',
        'data/stock_picking_type_group_data.xml'
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
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
}
