# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2023 odooAi.cn

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

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
    'name': 'Odoo Module Sample. App sample with widget. Odoo开发规范模板',
    'version': '15.23.10.07',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'OPL-1',
    'sequence': 2,
    'price': 2.00,
    'currency': 'EUR',
    'images': ['static/description/banner.gif'],
    'summary': '''
    Odoo module template. module sample with 170+ widget list. Clone this sample to your name to quick create your odoo addons.
    Developer reference guides, Developer Tutorials.
    Sample manifest, .py, .xml views and data. report, action, menu..
    ''',
    'description': '''
    Just Rename the sample app to your name to quick create new module.
    All file follow odoo rule with comments.
    Support Odoo 17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition
    Odoo Developr rule from here 
    https://www.odooai.cn/documentation/16.0/developer.html
    1. A full Sample module app of odoo addons. All the code, views, data ,banner, icon and description sample follow the odoo rule.
    2. Sample manifest file. Including structure and name and description etc, all field sample. Security xml and csv file for role group access rule.
    Sample icon, banner, index.html, install/uninstall hooks.
    Follow most odoo rule follow
     https://www.odooai.cn/documentation/16.0/contributing/development/coding_guidelines.html
    3. Sample .py models file, for new model and inherit model
    4. Sample .xml views file for models, with list, kanban, form, search
    5. Sample controllers file for website data publish and api developer. including how inherit odoo portal home.
    6. Sample report design file. .py file with how sql define. .xml file for graph and pivot.
    7. Sample action and menu file. Root menu and menu group and action menu.
    8. Ui misc sample. Alert like info and special field setup.
    9. Odoo Widget sample. 170+ widget list document and Frequently Used Sample.
    10. Quick access odoo developer Tutorials online. Document online for chinese and english. Fast visit in China.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ========== 中文说明
    1. 一个完整的odoo插件模块应用程序示例，所有代码、视图和数据都遵循odoo规则
    2. Manifest示例清单文件。包括结构、名称和描述等所有字段样例。安全xml和csv文件用于控制访问规则
    全部遵循odoo规则 https://www.odooai.cn/documentation/16.0/zh_CN/developer/reference/backend/module.html#reference-module-manifest
    3. .py 示例文件，包括新模型和继承模型的示例
    4. .xml 示例视图文件，包括列表、看板、表单、搜索等
    5. controllers 示例文件，用于门户网站对外数据发布及 api 接口开发。例子包含对 odoo portal 门户的继承处理
    6. report报告设计文件示例。包括如何定义 sql 生成视图的.py文件，用于 graph 和 pivot的.xml文件。
    7. action 动作 和 menu 菜单文件示例。
    8. 特殊Ui样例，包括 Alert role 信息及特殊字段展现设置。
    9. Odoo Widget 使用指导，包括 170+小部件清单，常用 widget 用法。
    10.快速访问在线Odoo开发人员教程。
    11. 多语言支持，多公司支持
    12. Odoo 17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
    ''',
    'depends': [
        'app_common',
        'account',
        # 'website',
    ],
    'data': [
        # please add your file
        # please comment follow on ur produce odoo
        'security/app_security.xml',
        'security/ir.model.access.csv',
        'views/model_new_views.xml',
        'report/model_new_report_views.xml',
        'views/menu_views.xml',
        # 'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'app_/static/src/scss/style.scss',
        ],
        'web.assets_backend': [
            # 'app_/static/src/js/*.js',
        ],
    },
    'demo': [
        'data/model_new_demo.xml',
        # 'views/website_templates.xml',
    ],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
