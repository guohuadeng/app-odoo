# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': "活动高级搜索导航,Event Advance Search Superbar",
    'version': '19.0.25.06.10',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': "按活动阶段和标签分类树状导航浏览活动。Browse events by stage and tag category with Superbar tree navigator.",
    'description': """
    1. Superbar tree navigator for Event Event with stage_id and company_id.
    2. Superbar tree navigator for Event Tag with category_id.
    3. Support list view, kanban view, pivot view, graph view and calendar view.
    4. Multi-select tree nodes with Ctrl/Cmd, include or exclude child nodes.
    5. Free plugin for app_web_superbar, no extra purchase needed.
    6. Multi-language Support. Multi-Company Support.
    7. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    8. Full Open Source.

    1. 活动按阶段和公司树状导航浏览
    2. 活动标签按分类树状导航浏览
    3. 支持列表、看板、透视表、图表、日历等多种视图
    4. Ctrl/Cmd多选树节点，勾选控制是否包含子节点
    5. app_web_superbar免费插件，无需额外购买
    6. 多语言支持，多公司支持
    7. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    8. 代码完全开源
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'event',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/event_event_views.xml',
        'views/event_tag_views.xml',
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
