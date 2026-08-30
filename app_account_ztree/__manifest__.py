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
    'name': "多层级会计科目树,Account Multi Level Chart Tree",
    'version': '19.0.26.04.22',
    'author': 'odooai.cn',
    'category': 'Accounting/Accounting',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': "会计科目多层级父子树状选择器，zTree widget。Multi Level Account Chart tree with parent-children zTree widget for list select navigator.",
    'description': """
    1. zTree widget for Account Chart with parent-children hierarchy tree.
    2. Advance search with real parent-children tree in ListView or KanbanView.
    3. Easy to setup with widget='widget_select' and XML parameters.
    4. Support ztree_parent_key, ztree_expend_level, limit, order parameters.
    5. Reusable widget for any parent-child relationship model.
    6. Multi-language Support. Multi-Company Support.
    7. Support Odoo 18, 17, 16, 15, 14, 13, 12, Enterprise and Community and odoo.sh Edition.
    8. Full Open Source.

    1. 会计科目多层级父子树状选择器，zTree widget
    2. 在列表或看板视图中通过父子树进行高级搜索
    3. 使用 widget='widget_select' 和 XML 参数轻松配置
    4. 支持 ztree_parent_key、ztree_expend_level、limit、order 参数
    5. 可复用的通用父子关系树控件
    6. 多语言支持，多公司支持
    7. Odoo 18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    8. 代码完全开源
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'account',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
        'views/res_company_views.xml',
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
