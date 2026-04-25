# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# description:

{
    'name': '库存位置树控件 / Stock Location zTree Parent Children Tree',
    'version': '18.0.24.12.09',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '库存位置父子树选择器，在many2one字段中显示树状层级 / Stock location parent children tree selector in many2one field',
    'description': """
1. zTree widget for stock location parent children tree in many2one select.
2. Advance search with real parent children tree in ListView or KanbanView.
3. Support stock location, product category and department tree.
4. Easy to customize widget parameters for tree level, limit, order.
5. Multi-Language Support.
6. Multi-Company Support.
7. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
8. Full Open Source under LGPL-3 license.
1. zTree 控件实现库存位置在 many2one 字段中的父子树选择器。
2. 在列表和看板视图中进行父子树高级搜索。
3. 支持库存位置、产品分类和部门树。
4. 可自定义树控件参数，包括展开层级、记录限制、排序方式。
5. 多语言支持。
6. 多公司支持。
7. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
8. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'stock',
    ],
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'data': [
        'views/stock_views.xml',
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
