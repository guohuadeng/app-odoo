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
    'name': 'App Web Responsive Fullwidth (form view full width)',
    'version': '12.0.1.2',
    'category': 'web',
    'author': 'Sunpop.cn',
    'website': 'http://www.sunpop.cn',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """
    Form view Responsive full width (fullwidth). Ready for small, medium, large, extra large screen.Ready for enterprise and communicate version.
    """,
    'description': """
    UI Enhance for Odoo. Form view fullwidth, full screen.
    ready
    """,
    'depends': [
        'web'
    ],
    'data': [
        'views/template_view.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    "price": 18.00,
    "currency": "EUR",

    'images': ['static/description/banner.png'],

    'installable': True,
    'auto_install': False,
    'application': True,
}
