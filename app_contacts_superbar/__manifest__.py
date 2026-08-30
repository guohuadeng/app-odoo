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
    'name': '通讯录联系人超级导航 / Contacts Partner Superbar',
    'version': '19.0.25.08.15',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按公司、类别、行业树状浏览联系人 / Browse contacts by company, category and industry with hierarchical tree navigator',
    'description': """
1. Navigate contacts by company hierarchy with parent-children tree structure.
2. Filter contacts by partner category with multi-select and counters.
3. Filter contacts by industry type for quick segmentation.
4. Multi-company grouping support for enterprise deployment.
5. Support list, kanban, pivot and graph views.
6. One-click toggle to show or hide superbar panel.
7. Multi-node selection with Ctrl(Windows) / Cmd(Mac).
8. Easy to customize with searchpanel extra params.

1. 按公司父子公司关系树状浏览联系人。
2. 按合作伙伴类别筛选，支持多选和计数。
3. 按行业类型快速筛选联系人。
4. 多公司分组支持，适配企业级部署。
5. 支持列表、看板、透视和图表视图。
6. 一键切换显示或隐藏超级导航栏。
7. 支持 Ctrl(Windows) / Cmd(Mac) 多选节点。
8. 可通过 searchpanel 参数灵活定制。

9. Multi-language support for global teams.
10. Full version support: Odoo 19, 18, 17, 16, 15, 14, 13, 12.
11. Full open source under LGPL-3 license.

9. 多语言支持，适配全球团队。
10. 全版本支持：Odoo 19, 18, 17, 16, 15, 14, 13, 12。
11. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'contacts',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/res_partner_views.xml',
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
