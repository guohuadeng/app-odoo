# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': "App crm browse by stage and team",
    'version': '13.19.09.27',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': """
    Browse crm lead by stage and team. Use for parent children tree list kanban navigator. 
    ztree widget.Hierarchy Tree.Parent Children relation tree..
    """,
    'description': """
    Superbar, zTree widget. 
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    eg: Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'crm',
        'utm',
    ],
    'images': ['static/description/crm1.jpg'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
