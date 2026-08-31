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
    'name': '通讯录联系人超级导航专业版 / Contacts Superbar Pro',
    'version': '19.0.24.12.04',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '增强版联系人导航，新增公司类型和日期范围搜索 / Enhanced contacts navigator with company type and date range search',
    'description': """
1. Inherits all features from app_contacts_superbar.
2. Company type (is_company) filter for contacts.
3. Date range search by creation date.
4. Partner category multi-select with counters.
5. Industry type navigation.
6. Multi-company grouping support.
7. Support list, kanban, pivot and graph views.

1. 继承 app_contacts_superbar 全部功能。
2. 按公司类型（公司/个人）筛选联系人。
3. 按创建日期范围搜索联系人。
4. 按合作伙伴类别多选筛选并显示计数。
5. 按行业类型导航筛选。
6. 多公司分组支持。
7. 支持列表、看板、透视和图表视图。

8. Multi-language support for global teams.
9. Full version support: Odoo 19, 18, 17, 16, 15, 14, 13, 12.
10. Full open source under LGPL-3 license.

8. 多语言支持，适配全球团队。
9. 全版本支持：Odoo 19, 18, 17, 16, 15, 14, 13, 12。
10. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_contacts_superbar',
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
