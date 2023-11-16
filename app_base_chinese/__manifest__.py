# -*- coding: utf-8 -*-

# Created on 2023-02-02
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:


{
    'name': 'odoo中文版套件之基础,中国会计基础,Chinese Enhance All in One，',
    'version': '23.11.06',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0,
    'currency': 'EUR',
    'summary': '''
    odoo简体中文版全面增强. Chinese enhance. Out of the box use odoo in china. Chinese address format, number format, money format.
    Set all chinese default value. Default country, timezone, currency, partner.中国会计基础模块.
    ''',
    'description': '''
    odoo Chinese Enhance. odoo中国版增强-基础
    1. 中文地址格式，适用于所有中国中文客户、供应商、合作伙伴、用户、员工信息等
    2. 中文默认值，如国家、时区、货币等。处理模块 base, product.
    3. 客户加简称，地址显示中文化，客户编码显示优先
    4. 客户地址显示增加手机号与电话号码
    5. 货币处理，人民币增强，增加排序显示
    6. 修正品类的列表及m2o字段中不显示中文目录名的Bug
    7. 修正仓库位置的列表及m2o字段中不显示中文目录名的Bug
    8. 超级用户改时区为 中国
    9. 时间格式年月日为 中国格式，如 2023-08-08，时间为 12:34
    10. 国家增加排序，中国排第一 
    11. 收款相关显示中国习惯    
    12. 翻译导出默认中文，默认po
    13. [默认已移除，可自行加载.py]在 base 模型增加 name_en_US 字段，赋值后同时改翻译值
    14. 常用小数精度调整
    15. 销售团队改为中国
    16. 精简语言的显示，如 Chinese简体中文改为 中文
    21. 多语言支持，多公司支持
    22. Odoo 17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    23. 代码完全开源
    ======
    1. Chinese address format, applicable to all Chinese customers, suppliers, partners, users, employee information etc.
    2. Default values in Chinese such as country, time zone and currency. Processing module base, product.
    3. Add customer abbreviation and display addresses in Chinese; prioritize displaying customer codes.
    4. Display phone numbers along with mobile numbers for customer addresses.
    5. Currency processing with added sorting display.
    6. Fixed bug where the category list and m2o field did not display the name of the Chinese directory.
    7. Fixed bug where warehouse location list and m2o field did not display the name of the Chinese directory.
    8. Superuser changed time zone to China.
    9. Date format is year-month-day (e.g., 2023-08-08) and time is 12:34
    10.Country sorting added; China ranked first
    11.Display payment-related information according to typical practices in China.
    12.Default export translation is set to Mandarin (po).
    13.Added 'name_en_US' field in base model which updates translation value when assigned a value.
    14.Common decimal precision adjustments made.
    15.Sales team changed to [China].
    21. Multi-language Support. Multi-Company Support.
    22. Support Odoo 17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    23. Full Open Source.
    ''',
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'depends': [
        'base_address_extended',
        'account',
        'sales_team',
        'sale',
        'stock',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.jpg'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_currency_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/ir_default_views.xml',
        # 'views/templates.xml',
        'wizard/sale_make_invoice_advance_views.xml',
        'data/ir_default_data.xml',
        'data/base_data.xml',
        'data/decimal_precision_data.xml',
        'data/res_country_data.xml',
        'data/res_currency_data.xml',
        'data/res_lang_data.xml',
        'data/res_company_data.xml',
        'data/res_partner_data.xml',
        'data/res_users_data.xml',
        'data/product_data.xml',
        'data/product_pricelist_data.xml',
        'data/stock_location_data.xml',
        'data/sales_team_data.xml',
        'views/ir_module_module_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_base_chinese/static/src/scss/app_style.scss',
        ]
    },
    'demo': [
        'data/res_company_demo.xml',
        'data/res_partner_demo.xml',
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
