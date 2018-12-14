# -*- coding: utf-8 -*-

# Created on 2018-11-05
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
    'name': "App base chinese，中国化基本模块增强",
    'version': '12.0.12.09',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Chinese enhance. Out of the box use in china.
    Set all chinese default value.
    Default country, timezone, currency, partner... 
    """,
    'description': """
    
    odoo Chinese Enhance. 中国化增强-基础
    1. 中文默认值，如国家、时区、货币等。处理模块 base, product.
    2. 客户加简称，地址显示中文化，客户编码显示优先
    3. 货币处理，增加排序显示
    4. todo:中文演示数据(只有demo模式才加载)
    
    """,
    'pre_init_hook': 'pre_init_hook',
    'depends': [
        'base',
        'product',
        'l10n_cn'
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_category_views.xml',
        'views/res_partner_views.xml',
        'views/res_currency_views.xml',
        'data/ir_default_data.xml',
        'data/ir_sequence_data.xml',
        'data/base_data.xml',
        'data/res_country_data.xml',
        'data/res_currency_data.xml',
        'data/product_data.xml',
        'data/product_pricelist_data.xml',
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
    'installable': True,
    'application': True,
    'auto_install': False,
}
