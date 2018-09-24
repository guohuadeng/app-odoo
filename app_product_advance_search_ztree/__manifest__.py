# -*- coding: utf-8 -*-
##############################################################################
#
#    odtree
#    author:15251908@qq.com (openliu)
#    license:'LGPL-3
#
##############################################################################

# Created on 2018-09-25
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': 'Product Advance search with category parent tree, zTree',
    'version': '11.0.9.29',
    'author': 'Sunpop.cn',
    'category': 'Sales',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Advance search with real parent tree Structure, ListView or Kanban View ,
    eg: Product category tree ,Department tree
    """,
    'description': """
    Advance search with real parent tree, ListView or KanbanView ,
    eg: Product category tree ,Department tree
    超级方便的产品查询，可以快速按产品目录过滤。
    """,
    'price': 98.00,
    'currency': 'EUR',
    'depends': [
        'app_web_search_advance_ztree', 'sale_management',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/product_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'js': [
    ],
    'images': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}

