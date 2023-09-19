# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 广州尚鹏，http://www.sunpop.cn
# email: 75695762@qq.com
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
    'name': "App Purchase Batch Procurement, Procurement product set supplier",
    'version': '10.0.2.14',
    'summary': """App Purchase Batch Procurement, Procurement product set supplier""",
    'description': """
    1. Product batch reorder, create procurement
    产品批量补货
    2. Procurement batch setup supplier, quick purchase    
    补货单快速设置供应商，直接生成采购询价单。
    3. Product filter virtual view (available/exhausted/negative)
    产品在途库存过滤
    4. Multi language support, done for Chinese and English
    多语言版本，默认支持中英双语
    """,
    'author': '广州欧度智能',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'category': 'Purchase',
    'sequence': 0,
    'pre_init_hook': 'pre_init_hook',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'stock', 'purchase'],
    'data': [
        'views/asset_views.xml',
        'views/procurement_order_views.xml',
        'views/product_template_views.xml',
        'views/menus.xml',
        'wizard/product_set_supplier_views.xml',
        'wizard/procurement_batch_generator_view.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/tree_view_btn.xml'
    ],
    'js': [
    ],
    "price": 68.00,
    "currency": "EUR",
    'installable': True,
    'auto_install': False,
    'application': True,
}
