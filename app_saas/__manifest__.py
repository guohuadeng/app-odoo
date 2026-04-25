# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2026 odooAi.cn

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# 行业应用说明，应该是带 Industry 的就会放入

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
    'name': "SaaS云服务客户端 / odooapp.cn SaaS Client - Ai Passport",
    'summary': 'AiSaas云服务，Ai通行证全社交媒体SSO登录，中文翻译更新，模块更新推送。/ AiSaas cloud service with Ai Passport SSO login, Chinese translation update and module update push.',
    'description': '''
    1. Ai通行证实现全社交媒体登录支持
    2. 快速访问Odoo中文应用商店并获取独享Odoo中文通行码，可随时断开云服务连接
    3. 一键获取最新Odoo中文应用模块与主题，最新行业服务包
    4. 一键获取Odoo中文翻译更新（会员专属）
    5. 快速获取Odoo服务，Odoo升级评估
    6. 系统出错时一键提交，获取技术支持（会员专属）
    7. 注意，odoo默认新用户都是门户用户，不给访问内部管理内容
    11.多语言支持，多公司支持
    12.仅从Odoo18-16企业版，社区版版本开始支持
    13.代码完全开源
    ''',
    'depends': [
        'app_common',
        'auth_oauth',
        # 'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/auth_oauth_provider_data.xml',
        'data/ir_config_parameter.xml',
        'views/auth_oauth_provider_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_users_views.xml',
        'wizard/error_submit_wizard_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'app_/static/src/scss/style.scss',
        ],
        'web.assets_backend': [
            'app_saas/static/src/js/error_dialog_extend.js',
            'app_saas/static/src/xml/error_dialog_extend.xml',
            'app_saas/static/src/js/error_submit_form_view.js',
        ],
    },
    'demo': [
    ],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
