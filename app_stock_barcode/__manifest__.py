# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 广州尚鹏，http://www.sunpop.cn
# email: 75695762@qq.com
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
    'name': "App Warehouse Management Barcode Enhance",
    'version': '10.0.1',
    'summary': """条码，仓库模块操作增强""",
    'description': """
    扫码面板
    """,
    'author': 'Sunpop.cn',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'category': 'Warehouse',
    'sequence': 0,
    'pre_init_hook': 'pre_init_hook',
    'depends': ['stock_barcode'],
    'data': [
        'views/stock_pack_current_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_quant_package_views.xml',
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
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
