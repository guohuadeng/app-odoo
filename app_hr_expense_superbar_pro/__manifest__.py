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
    'name': "Hr Expense Superbar Pro",
    'version': '19.0.26.05.20',
    'author': 'odooai.cn',
    'category': 'Human Resources',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Browse hr expense by departments or Analytic Account.
    Easy to navigator and browse any data. Support list, kanban, pivot, graph view.
    ztree widget. hr Hierarchy organization chart Tree.
    """,
    'description': """
    Superbar, zTree widget.
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    eg: Product category tree ,Department tree, stock location tree.
    按部门或分析项目查看报销，超级方便的查询。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'app_hr_expense_superbar',
        # o19：hr.expense.sheet 模型与 sheet 搜索视图由 app_hr_expense_pro 兼容层提供，
        # 本模块 sheet 侧栏视图 inherit_id 引用兼容层 xmlid，必须声明依赖保证加载顺序
        'app_hr_expense_pro',
    ],
    'images': ['static/description/hr2.gif'],
    'data': [
        'views/hr_expense_views.xml',
        'views/hr_expense_sheet_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
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
