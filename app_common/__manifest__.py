# -*- coding: utf-8 -*-

# Created on 2023-02-02
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
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "欧度智能基础功能及面板,odooAi Common Util and Tools",
    'version': '18.0.26.05.29',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': "odooai.cn应用核心基础模块，提供通用工具函数和面板。Core module for odooai.cn apps with common utilities and tools.",
    'description': '''
    1. Quick import data from excel with .py code.
    2. Quick m2o default value helper.
    3. Filter for useless field.
    4. UTC local timezone convert.
    5. Get browser user-agent.
    6. Image to local, image URL to local, media to local attachment.
    7. Log cron job management.
    8. Boost for less no-use mail.
    9. Customize .rng file.
    10. Misc utilities like get distance between two points.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.

    Setup: server_wide_modules = web,app_common

    1. 通过.py代码快速从Excel导入数据
    2. Many2One默认值快捷设置
    3. 无用字段过滤器
    4. UTC本地时区转换
    5. 获取浏览器User-Agent
    6. 图片转本地、图片URL转本地、媒体转附件
    7. 日志定时任务管理
    8. 减少无用邮件提升性能
    9. 自定义.rng文件
    10. 通用工具如计算两点距离等
    11. 多语言支持，多公司支持
    12. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
    ''',
    'depends': [
        'mail',
        'base_setup',
        'web',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'data/ir_module_category_data.xml',
        'wizard/mail_compose_message_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_cron_views.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    # 可以不需要，因为直接放 common中了
    # 'external_dependencies': {'python': ['pyyaml', 'ua-parser', 'user-agents']},
    'installable': True,
    'application': True,
    'auto_install': True,
}
