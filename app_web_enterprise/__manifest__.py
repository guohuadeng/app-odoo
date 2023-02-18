# -*- coding: utf-8 -*-

# Created on 2017-11-05
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
    'name': "App web enterprise enhance,企业版界面增强",
    'version': '16.23.02.19',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    odoo enterprise version UI theme enhance.
    1. Add dropdown arrow to parent menu.
    2. Replace the odoo logo to your company logo in main menu.
    3. Alway show search in main menu.
    """,
    'description': """
    odoo enterprise version UI enhance.
    广州尚鹏，Sunpop.cn 的odoo模块。企业版界面增强。
    1. Add dropdown arrow to parent menu.
    多级菜单中出现箭头。
    2. Replace the odoo logo or url to your company in menu and page.
    替换主菜单界面的logo为你公司的logo。
    3. Alway show search in main menu.
    在主菜单界面让搜索可见。
    4. Fix view bug like graph shake.
    修正原生样式bug，如Graph会抖动。
    """,
    'price': 68.00,
    'currency': 'EUR',
    'depends': [
        'mail',
        'web_enterprise',
        # 'web_mobile'
    ],
    'images': [],
    'data': [
    ],
    'assets': {
        'web.assets_qweb': [
            'app_web_enterprise/static/src/xml/*.xml',
        ],
        # 企业版变色，注意这个是变量定义，要before
        'web._assets_primary_variables': [
            ('before', 'web_enterprise/static/src/scss/primary_variables.scss', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            ('before', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_before.scss'),
            ('after', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_after.scss'),
            'app_web_enterprise/static/src/components/*/*.xml',
            'app_web_enterprise/static/src/webclient/**/*.xml',
            'app_web_enterprise/static/src/xml/**/*.xml',
            # 'app_web_enterprise/static/src/xml/base.xml',
        ],
        # 这里是改样式，要 after处理
        'web.assets_common': [
            ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
        ],
        'web.assets_frontend': [
            # ('after', 'web/static/src/core/**/*', 'app_web_enterprise/static/src/xml/base.xml'),
            ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
        ],
    },

    # 'demo': [
    # ],
    # 'test': [
    # ],

    'images': ['static/description/app_web_enterprise_03.jpg'],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': True,
}
