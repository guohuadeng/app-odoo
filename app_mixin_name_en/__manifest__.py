# -*- coding: utf-8 -*-

# Created on 2018-11-05
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
    'name': "mixin english name，增加英文名字段",
    'version': '13.20.05.11',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0,
    'currency': 'EUR',
    'summary': """
    Chinese enhance. Out of the box use in china.
    Set all chinese default value.
    Add quick set of english name.
    Default country, timezone, currency, partner... 
    """,
    'description': """
    
    odoo Chinese Enhance. 中国化增强-基础
    1. mixin, 增加英文名字段, 自动设定lang=en_US的名称为英文名  
    2
    """,
    'depends': [
        'base',
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_views.xml',
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
