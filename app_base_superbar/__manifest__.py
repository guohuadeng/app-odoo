# -*- coding: utf-8 -*-

# Created on 2018-08-15
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
    'name': "基础管理快速导航,Easy Admin Navigator with Superbar",
    'version': '19.0.25.04.13',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': "菜单/视图/字段/动作/用户等管理项快速树状导航。Quick admin navigator for menu, views, fields, actions, users with Superbar tree.",
    'description': """
    1. Superbar tree navigator for admin settings: menus, views, fields, actions, reports, server actions, attachments, defaults, access rights, constraints, users.
    2. Navigate and search technical settings by category tree with list/kanban/pivot/graph views.
    3. Support parent-children hierarchy, Ctrl/Cmd multi-select, child node inclusion control.
    4. Multi-language Support. Multi-Company Support.
    5. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    6. Full Open Source.

    1. 菜单、视图、字段、动作、报表、服务端动作、附件、默认值、权限、约束、用户等管理项树状导航
    2. 按分类树浏览和搜索技术设置
    3. 支持父子层级、Ctrl/Cmd多选、子节点包含控制
    4. 多语言支持，多公司支持
    5. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    6. 代码完全开源
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'web',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        # 'views/res_groups_views.xml',
        'views/ir_actions_act_window_views.xml',
        'views/ir_actions_actions_views.xml',
        'views/ir_actions_report_views.xml',
        'views/ir_actions_server_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_default_views.xml',
        'views/ir_model_access_views.xml',
        'views/ir_model_constraint_views.xml',
        'views/ir_model_fields_views.xml',
        'views/ir_ui_menu_views.xml',
        'views/ir_ui_view_views.xml',
        'views/res_users_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
