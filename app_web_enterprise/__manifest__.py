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
    'name': "!odoo18 Enterprise enhance Pack,企业版界面及操作增强",
    'version': '18.0.25.09.16',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Ui Enhance pack of odoo Enterprise version. OEM Pack for odoo theme. Support mobile theme and dark mode theme.
    """,
    'description': """
    odoo enterprise version UI enhance.
    欧度智能，odooai.cn 的odoo模块。企业版界面增强。
    1. Ui Enhance pack of odoo Enterprise version. Use comfortable green color
    odoo企业版界面增强套件，更方便操作。使用更舒适护眼的绿色作为主色。
    2. Add dropdown arrow to parent menu group.
    多级菜单中出现箭头，导航操作更方便。
    3. Replace the odoo logo or url to your company in menu and page.
    替换主菜单界面的logo为你公司的logo。
    4. Add underline for input field.
    在可编辑字段下方增加下划线，易于分辨。
    5. Add grid line form list view. Easy to read list data.
    为表格list增加行列分隔线，易于看数据。
    6. Add grid line to Account Reports. Easy to view Data.
    为财务报表增加行列分隔线，易于看数据及对账。
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    """,
    'price': 68.00,
    'currency': 'EUR',
    'depends': [
        'app_odoo_customize',
        'web_enterprise',
        # 'web_mobile'
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        # 企业版变色，注意这个是变量定义，要before，应该是理解为 元素1 在元素2的前面
        'web._assets_primary_variables': [
            ('before', 'web_enterprise/static/src/scss/primary_variables.scss', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            ('before', 'web_enterprise/static/src/webclient/home_menu/home_menu.variables.scss', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
            ('before', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_before.scss'),
            ('after', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_after.scss'),
            ('after', 'web_enterprise/static/src/webclient/navbar/navbar.variables.scss', 'app_web_enterprise/static/src/webclient/navbar.variables.scss'),
            ('after', 'web_enterprise/static/src/webclient/navbar/navbar.scss', 'app_web_enterprise/static/src/webclient/navbar.scss'),
            'app_web_enterprise/static/src/webclient/**/*.xml',
            'app_web_enterprise/static/src/xml/res_config_edition.xml',
            # 'app_web_enterprise/static/src/xml/form.xml',
        ],
        # 黑夜模式
        "web.dark_mode_variables": [
            ('remove', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
            ('before', 'web_enterprise/static/src/scss/primary_variables.dark.scss', 'app_web_enterprise/static/src/scss/primary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('remove', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
            ('remove', 'app_web_enterprise/static/src/webclient/navbar.variables.scss'),
            ('remove', 'app_web_enterprise/static/src/webclient/navbar.scss'),
        ],
        # 这里是改样式，要 after处理
        'web.assets_frontend': [
            ('before', 'web_enterprise/static/src/webclient/home_menu/home_menu.variables.scss', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
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
