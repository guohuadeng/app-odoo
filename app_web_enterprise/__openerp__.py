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
    'name': "App web enterprise enhance, odoo企业版界面增强",
    'version': '10.0.5.17',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    odoo enterprise version UI enhance.
    广州尚鹏，Sunpop.cn 的odoo模块。企业版界面增强。
    1. Add dropdown arrow to parent menu.
    多级菜单中出现箭头。
    2. Replace the odoo logo to your company logo in main menu.
    替换主菜单界面的logo为你公司的logo。
    3. Alway show search in main menu. 
    在主菜单界面让搜索可见。
    """,
    'description': """
    模块开发模板，目录结构与文件定义。
    """,
    'price': 98.00,
    'currency': 'EUR',
    'depends': ['web_enterprise'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'js': [
    ],
    'images': ['static/description/app_web_enterprise_03.jpg'],
    'pre_init_hook': 'pre_init_hook',
    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
