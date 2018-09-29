# -*- coding: utf-8 -*-
# author: 'Nilesh Sheliya',

# Created on 2018-09-30
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
    'name': "App Row Number in tree list view",
    'version': '11.0.9.30',
    'summary': 'Show row number in tree/list view. list number, list row number',
    'category': 'Other',
    'description': """By installing this module, user can see row number in Odoo backend tree view.""",
    'author': 'Sunpop.cn',
    "depends": ['web'],
    'data': [
        'views/listview_templates.xml',
    ],
    "images": ["static/description/screen1.png"],
    'license': 'LGPL-3',
    'qweb': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
