# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2026 odooAi.cn

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
    'name': 'Odoo 模块开发模板 / Odoo Module Sample with Widget',
    'version': '18.0.24.12.26',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 2.00,
    'currency': 'EUR',
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'summary': 'Odoo模块开发模板，含170+Widget清单与使用样例 / Odoo module template with 170+ widget list and developer sample code',
    'description': """
1. A full Sample module app of odoo addons. All the code, views, data, banner, icon and description sample follow the odoo rule.
2. Sample manifest file including structure, name, description and all field samples. Security XML and CSV file for role group access rule.
3. Sample .py models file for new model and inherit model.
4. Sample .xml views file for models with list, kanban, form, search.
5. Sample controllers file for website data publish and API developer including how to inherit odoo portal home.
6. Sample report design file with SQL define in .py and graph/pivot in .xml.
7. Sample action and menu file with root menu and menu group.
8. UI misc sample with alert info and special field setup.
9. Odoo Widget sample with 170+ widget list document and frequently used sample.
10. Quick access odoo developer tutorials online for Chinese and English.
11. Multi-language Support.
12. Multi-Company Support.
13. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
14. Full Open Source under LGPL-3 license.
1. 一个完整的 Odoo 插件模块应用程序示例，所有代码、视图和数据都遵循 Odoo 规则。
2. Manifest 示例清单文件，包括结构、名称和描述等所有字段样例。安全 XML 和 CSV 文件用于控制访问规则。
3. .py 示例文件，包括新模型和继承模型的示例。
4. .xml 示例视图文件，包括列表、看板、表单、搜索等。
5. Controllers 示例文件，用于门户网站对外数据发布及 API 接口开发，包含对 Odoo Portal 门户的继承处理。
6. Report 报告设计文件示例，包括如何定义 SQL 生成视图的 .py 文件，用于 graph 和 pivot 的 .xml 文件。
7. Action 动作和 Menu 菜单文件示例，含根菜单和菜单组。
8. 特殊 UI 样例，包括 Alert 信息及特殊字段展现设置。
9. Odoo Widget 使用指导，包括 170+ 小部件清单，常用 Widget 用法。
10. 快速访问在线 Odoo 开发人员教程，中英文文档，国内快速访问。
11. 多语言支持。
12. 多公司支持。
13. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
14. 代码完全开源，基于 LGPL-3 协议。
    """,
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
