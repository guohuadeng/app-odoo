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
    'name': "App web enterprise enhance,企业版界面增强",
    'version': '16.23.04.08',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
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
    欧度智能，odooai.cn 的odoo模块。企业版界面增强。
    1. Add dropdown arrow to parent menu.
    多级菜单中出现箭头。
    2. Replace the odoo logo or url to your company in menu and page.
    替换主菜单界面的logo为你公司的logo。
    3. Add underline for input field.
    在可编辑字段下方增加下划线，易于分辨。
    4. Add grid line form list view. Easy to read list data.</li>
    为表格list增加行列分隔线，易于看数据。
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
        'views/webclient_templates.xml',
    ],
    'assets': {
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
            ('after', 'web/static/lib/jquery.ui/jquery-ui.css', 'app_web_enterprise/static/lib/jquery.ui/jquery-ui.css'),
            ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
        ],
        'web.assets_frontend': [
            # ('after', 'web/static/src/core/**/*', 'app_web_enterprise/static/src/xml/base.xml'),
            ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
            'app_web_enterprise/static/src/scss/app_style_website.scss',
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
