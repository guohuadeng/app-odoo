# -*- coding: utf-8 -*-

# Created on 2017-11-05
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
    'name': 'MRP BOM Location for Manufacturing/Unbuild Order',
    'version': '10.0.7.24',
    'author': 'Sunpop.cn',
    'category': 'Manufacturing',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': 'Adds location field to Bill of Materials and its components. Done for Manufacturing/Unbuild Order',
    'description': """
    模块开发模板，目录结构与文件定义。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': ['mrp'],
    'images': ['static/description/banner.png'],
    'data': [
        "views/mrp_view.xml",
        "views/report_mrpbomstructure.xml",
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
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
