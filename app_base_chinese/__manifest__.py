# -*- coding: utf-8 -*-

# Created on 2018-11-05
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
    'name': "App base chinese，中国化基本模块增强",
    'version': '13.20.09.19',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
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
    1. 中文默认值，如国家、时区、货币等。处理模块 base, product.
    2. 客户加简称，地址显示中文化，客户编码显示优先
    3. 客户地址显示增加手机号与电话号码
    4. 货币处理，增加排序显示
    5. 用户名支持翻译（可能会增加复杂度，后续看）
    6. 修正品类的列表及m2o字段中不显示中文目录名的Bug
    7. 修正仓库位置的列表及m2o字段中不显示中文目录名的Bug
    8. 超级用户改时区为 中国
    9. 时间格式年月日为 2019-12-30，时间为 22:10
    10. 国家增加排序，中国排第一 
    11. 收款相关显示中国习惯    
    12. 翻译导出默认中文，默认po
    13. 在 base 模型增加 name_en_US 字段，赋值后同时改翻译值
    14. 常用小数精度调整
    21. todo:中文演示数据(只有demo模式才加载)    
    """,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'depends': [
        'app_base',
        'account',
        'stock',
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_currency_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/ir_default_views.xml',
        'views/templates.xml',
        'wizard/sale_make_invoice_advance_views.xml',
        'data/ir_default_data.xml',
        'data/base_data.xml',
        'data/decimal_precision_data.xml',
        'data/res_country_data.xml',
        'data/res_currency_data.xml',
        'data/res_lang_data.xml',
        'data/product_data.xml',
        'data/product_pricelist_data.xml',
        'data/stock_location_data.xml',
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
    'installable': True,
    'application': True,
    'auto_install': False,
}
