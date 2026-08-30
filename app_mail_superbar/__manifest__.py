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
    'name': "邮件高级搜索 / Mail Quick Navigator",
    'version': '19.0.24.11.12',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': '按多种分类浏览邮件，Superbar高级搜索。/ Browse and search all mail by category with Superbar advance search.',
    'description': """
English Features:
1. Superbar and zTree widget for Mail module advance search.
2. Quick mail navigator with search by all kinds of category.
3. Support message, mail, channel partner, mail followers and mail tracking value search.
4. Advance search sidebar for many2one, many2many, date range, boolean, selection, number fields.
5. Search sidebar available for list, kanban, pivot and graph views.
6. Support navigate in search more windows for m2o or m2m fields.
7. Easy customize for any app with extra param for searchpanel.
8. Multi-language Support. Multi-Company Support.
9. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
10. Full Open Source.

中文功能：
1. 邮件模块Superbar和zTree高级搜索组件。
2. 快速邮件导航器，支持按各种分类搜索。
3. 支持消息、邮件、频道成员、邮件关注者和邮件跟踪值的搜索。
4. 高级搜索侧栏，支持many2one、many2many、日期范围、布尔、选择、数字字段。
5. 搜索侧栏支持列表、看板、数据透视和图表视图。
6. 支持在搜索更多窗口中为m2o/m2m字段导航筛选。
7. 易于自定义，支持searchpanel额外参数。
8. 多语言支持。多公司支持。
9. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
10. 代码完全开源。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'web',
        'mail',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/discuss_channel_member_views.xml',
        'views/mail_followers_views.xml',
        'views/mail_mail_views.xml',
        'views/mail_message_views.xml',
        'views/mail_tracking_value_views.xml',
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
