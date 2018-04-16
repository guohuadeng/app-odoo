# -*- coding: utf-8 -*-

# Created on 2017-11-05
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
    'name': "Purchase quantity fix if return(odoo 10 purchase order return bug fix)",
    'version': '10.0.3.24',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    odoo 10 purchase bug fix(return quantity error bug fix).
    odoo 10 采购退货后货物收到数量不正确，本模式对此bug进行了修复。
    """,
    'description': """
    We fix this bug in odoo 10.
    
    Steps to reproduce:
    Create a PO with product
    Validate a picking
    Say ‘oups is not the good PO :-(‘
    Make a return picking.
    Valide this return.
    -> The quantity received is not update (except Master)
    Make a return of return (to return in initial situation). (better than to do a copy of original to keep the link with purchase and parent picking).
    Validate partialy this return-return
    -> The quantity received is not update
    -> The action to show pickings doesn’t show the return-return picking
    """,
    'price': 98.00,
    'currency': 'EUR',
    'depends': ['purchase'],
    'images': [],
    'data': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'images': [
    ],
    'pre_init_hook': 'pre_init_hook',
    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
