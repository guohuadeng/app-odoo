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
    'name': "odoo Enterprise enhance Pack,企业版界面及操作增强",
    'version': '23.11.16',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Ui Enhance pack of odoo Enterprise version
    1. Add dropdown arrow to parent menu.
    2. Replace the odoo logo to your company logo in main menu.
    3. Alway show search in main menu.
    """,
    'description': """
    odoo enterprise version UI enhance.
    欧度智能，odooai.cn 的odoo模块。企业版界面增强。
    1. Ui Enhance pack of odoo Enterprise version
    odoo企业版界面增强套件，更方便操作
    2. Add dropdown arrow to parent menu group.
    多级菜单中出现箭头。
    3. Replace the odoo logo or url to your company in menu and page.
    替换主菜单界面的logo为你公司的logo。
    4. Add underline for input field.
    在可编辑字段下方增加下划线，易于分辨。
    5. Add grid line form list view. Easy to read list data.</li>
    为表格list增加行列分隔线，易于看数据。
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ==========
    1.
    2.
    11. 多语言支持，多公司支持
    12. Odoo 16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
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
        # 企业版变色，注意这个是变量定义，要before
        'web._assets_primary_variables': [
            ('before', 'web_enterprise/static/src/scss/primary_variables.scss', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
        ],
        # 处理header 变更
        'web.assets_backend': [
            ('before', 'web/static/src/webclient/navbar/navbar.scss', 'app_web_enterprise/static/src/scss/navbar_before.scss'),            # ('after', 'web/static/src/webclient/navbar/navbar.scss', 'app_web_enterprise/static/src/scss/navbar.scss'),
            ('after', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_after.scss'),
            # 'app_web_enterprise/static/src/components/*/*.xml',
            'app_web_enterprise/static/src/webclient/navbar.xml',
            'app_web_enterprise/static/src/xml/res_config_edition.xml',
            'app_web_enterprise/static/src/xml/form.xml',
        ],
        # 这里是改样式，要 after处理
        'web.assets_common': [
            # ('after', 'web/static/lib/jquery.ui/jquery-ui.css', 'app_web_enterprise/static/lib/jquery.ui/jquery-ui.css'),
            # ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
        ],
        'web.assets_frontend': [
            # ('after', 'web/static/src/core/**/*', 'app_web_enterprise/static/src/xml/base.xml'),
            # ('after', 'web_enterprise/static/src/webclient/home_menu/home_menu_background.scss', 'app_web_enterprise/static/src/scss/home_menu_background.scss'),
            # 'app_web_enterprise/static/src/scss/app_style_website.scss',
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
