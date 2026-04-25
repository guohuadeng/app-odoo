# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

{
    'name': 'CRM商机线索超级导航 / CRM Superbar',
    'version': '18.0.24.11.12',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': '按阶段、团队、营销活动树状浏览商机与线索 / Navigate CRM leads and opportunities by stage, team and campaign',
    'description': """
1. Navigate CRM opportunities by sales pipeline stage and team.
2. Navigate leads by UTM campaign, medium and source.
3. CRM report navigation with pivot and graph views.
4. Multi-company grouping support.
5. List and kanban view sidebar search panel.
6. Easy to customize with searchpanel extra params.

1. 按销售管道阶段和团队导航商机。
2. 按 UTM 营销活动、媒介和来源筛选线索。
3. CRM 报表支持透视和图表视图导航。
4. 多公司分组支持。
5. 列表和看板视图侧边栏搜索面板。
6. 可通过 searchpanel 参数灵活定制。

7. Multi-language support for global teams.
8. Full version support: Odoo 19, 18, 17, 16, 15, 14, 13, 12.
9. Full open source under LGPL-3 license.

7. 多语言支持，适配全球团队。
8. 全版本支持：Odoo 19, 18, 17, 16, 15, 14, 13, 12。
9. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'crm',
        'utm',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/crm_lead_views.xml',
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
