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
    'name': "项目任务导航 / Project &amp; Task Navigator",
    'version': '18.0.26.08.18',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按公司、客户、用户和阶段浏览项目和任务。/ Browse projects by company, partner, user and stage with Superbar.',
    'description': """
English Features:
1. Superbar and zTree widget for Project and Task advance search.
2. Browse projects by company, partner and user.
3. Browse project tasks by user, tags and stage.
4. Advance search sidebar for multiple field types.
5. Search sidebar available for list, kanban, pivot and graph views.
6. Multi-language Support. Multi-Company Support.
7. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
8. Full Open Source.

中文功能：
1. 项目和任务Superbar和zTree高级搜索组件。
2. 按公司、客户和用户浏览项目。
3. 按用户、标签和阶段浏览项目任务。
4. 高级搜索侧栏，支持多种字段类型。
5. 搜索侧栏支持列表、看板、数据透视和图表视图。
6. 多语言支持。多公司支持。
7. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
8. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'project',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/project_project_views.xml',
        'views/project_task_type_views.xml',
        'views/project_task_views.xml',
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
