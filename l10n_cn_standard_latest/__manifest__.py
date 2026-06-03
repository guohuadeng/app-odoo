# Copyright (C) 2008-2008 凯源吕鑫 lvxin@gmail.com
#                         维智众源 oldrev@gmail.com
# Copyright (C) 2012-2012 南京盈通 ccdos@intoerp.com
# Copyright (C) 2008-now  开阖软件 jeff@osbzr.com
# Copyright (C) 2017-now  jeffery9@gmail.com
# Copyright (C) 2018-now  欧度智能 https://www.odooai.cn

{
    'name': '2025最新中国会计科目表 / Latest Chinese Accounting Chart',
    'version': '18.0.26.03.06',
    'author': 'odooai.cn',
    'category': 'Accounting/Localizations/Account Charts',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': '2025最新中国会计科目表，营改增后会计科目调整，多级科目支持 / Latest Chinese accounting chart with multi-level account support',
    'description': """
1. 2025 latest Chinese accounting chart of accounts with post-VAT reform adjustments.
2. Updated to latest tax rates. Set menu to "Accounting".
3. Supplement classification and tag information.
4. Updated tax items with common Chinese VAT rate settings.
5. Support parent accounts with secondary account levels. Works with "app_web_widget_ztree" for tree navigation.
6. Use Kingdee naming convention for multi-level accounts separated by dots. Customizable account codes.
7. Must be installed in a clean environment without business data or existing accounts. Use "app_odoo_customize" to reset.
8. Including Chart of Accounts templates, Account templates, Tax templates.
9. Multi-Language Support.
10. Multi-Company Support.
11. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
12. Full Open Source under LGPL-3 license.
1. 2025 最新中国会计科目表，处理营改增后会计科目调整，更新至最新税率。
2. 将菜单设置为"财务"。
3. 补充分类及标签信息。
4. 更新税项信息，增加中国常用增值税率设定。
5. 可设置上级科目，支持二级科目。配合"app_web_widget_ztree"可增加树状导航。
6. 使用金蝶会计科目命名法对多级科目初始化，以点号分隔。可自行设定科目代码。
7. 必须在没有业务数据、没有会计科目的初始环境安装。可使用"app_odoo_customize"清除财务数据重置。
8. 包含科目表模板、科目模板、税金模板。
9. 多语言支持。
10. 多公司支持。
11. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
12. 代码完全开源，基于 LGPL-3 协议。
    """,
    'depends': [
        'app_account_ztree',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
        'report/account_report.xml',
        'report/report_voucher.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
