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
    'name': 'App Product Internal Type,Auto Sequence, Auto Code(Variants Supported)',
    'summary': 'Auto Internal Reference.',
    "version": '10.0.2.2',
    'category': 'Sales',
    'author': 'Sunpop.cn',
    'website': 'http://www.sunpop.cn',
    'license': 'AGPL-3',
    'sequence': 2,
    'installable': True,
    'auto_install': True,
    'application': True,
    'images': ['static/description/set2.jpg'],
    'currency': 'EUR',
    'price': 98,
    'description': u"""
        App Product Auto Sequence, Auto Code(Variants Supported)
    
        This module allows to associate a sequence to the product reference.<br/>
        The reference (default code) is unique (SQL constraint) and required.<br/>
        Support Product with or without Variants.
        1.Auto Sequence or code for every product.自动产品编码。
        2.Auto Sequence or for every product variants, like product20171130-001.自动多规格产品编码，形式为 主产品编码-001。
        3.Product code must be Unique.产品编码强制要求唯一。
        4.Define different product type, each product type use own rule of sequence.可自定义产品类型，不同产品类型使用不同编码规则。
        5.Quick access in sale , inventory, system menu.可以在销售、库存、系统菜单中快速定义。
        6.Multi language support.<br/>多语种支持。
        7.Setup default Auto Sequence for each product category
    """,
    'pre_init_hook': 'pre_init_hook',
    'depends': [
        'product',
        'stock',
        'sale',
        'purchase',
        'mrp',
                ],
    'data': [
        # 视图
        "security/ir.model.access.csv",
        "security/security.xml",
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/product_category_view.xml',
        'views/product_internal_type_view.xml',
        'data/product_sequence.xml',
    ],
    'demo': [
    ],
}
