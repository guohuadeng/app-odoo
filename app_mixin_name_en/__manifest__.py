# -*- coding: utf-8 -*-

{
    'name': "Product english name with Mixin，产品增加英文名字段-以Mixin方式的统一处理",
    'version': '18.0.26.05.13',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0,
    'currency': 'EUR',
    'summary': """
    Chinese enhance. Out of the box use in china.
    Set all chinese default value.
    Add quick set of english name.
    Default country, timezone, currency, partner... 
    """,
    'description': """
    odoo Chinese Enhance. 中国化增强-基础
    1. mixin, 增加英文名字段, 自动设定lang=en_US的名称为英文名
    """,
    'depends': [
        'product',
    ],
    'data': [
        'views/product_template_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
