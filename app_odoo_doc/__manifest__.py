# -*- coding: utf-8 -*-

# Created on 2022-09-01
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

##############################################################################
#    Copyright (C) 2009-TODAY odooAi.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "odoo用户手册开发手册大全,odoo User Doc & Developer Doc Anywhere",
    'version': '18.0.26.08.05',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'OPL-1',
    'sequence': 18,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/app_odoo_doc.gif'],
    'depends': [
        'web',
        'app_odoo_customize',
    ],
    'summary': '''
    Odoo用户手册与开发手册一键访问。1-Click access to Odoo user & developer documentation of current topic, with local branding.
    ''',
    'description': '''
    1. User Documentation and Developer documentation of Odoo.
    2. 1-Click to access help of current topic, current operation, current action via systray icon.
    3. Documentation with your company name and logo, fully localizable.
    4. Mrp doc, Sale doc, purchase doc, stock doc, account doc all in one.
    5. Configurable documentation root URL: host docs on your own server or use odooai.cn remote.
    6. Module kanban dropdown menu with "Help on Topic" action for quick access.
    7. Multi-language Support. Multi-Company Support.
    8. Support Odoo 18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    9. Full Open Source.
    ==========
    1. Odoo 的用户文档和开发人员文档。
    2. 一键点击即可访问当前主题、当前操作、当前菜单的帮助（系统托盘图标）。
    3. 附有您公司的名称和 Logo 的文档，完全可本地化。
    4. 集生产制造文档、销售管理文档、采购管理文档、库存管理文档和财务管理文档于一体。
    5. 可配置文档主域名：可在自有服务器托管文档或使用 odooai.cn 远程文档。
    6. 模块看板下拉菜单提供"查看当前帮助"操作，快速访问文档。
    7. 多语言支持，多公司支持
    8. Odoo 18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    9. 代码完全开源
    ''',
    'data': [
        'data/ir_config_parameter_data.xml',
        'data/ir_module_module_data.xml',
        'views/ir_module_module_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_odoo_doc/static/src/xml/doc_menu.xml',
            'app_odoo_doc/static/src/js/doc_menu.js',
        ],
    },
    'demo': [],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
