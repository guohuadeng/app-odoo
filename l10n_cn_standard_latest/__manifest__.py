# Copyright (C) 2008-2008 鍑簮鍚曢懌 lvxin@gmail.com
#                         缁存櫤浼楁簮 oldrev@gmail.com
# Copyright (C) 2012-2012 鍗椾含鐩堥€?ccdos@intoerp.com
# Copyright (C) 2008-now  寮€闃栬蒋浠?jeff@osbzr.com
# Copyright (C) 2017-now  jeffery9@gmail.com
# Copyright (C) 2018-now  娆у害鏅鸿兘 https://www.odooai.cn

{
    'name': '2025鏈€鏂颁腑鍥戒細璁＄鐩〃 / Latest Chinese Accounting Chart',
    'version': '19.0.26.07.16',
    'author': 'odooai.cn',
    'category': 'Accounting/Localizations/Account Charts',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': '2025鏈€鏂颁腑鍥戒細璁＄鐩〃锛岃惀鏀瑰鍚庝細璁＄鐩皟鏁达紝澶氱骇绉戠洰鏀寔 / Latest Chinese accounting chart with multi-level account support',
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
1. 2025 鏈€鏂颁腑鍥戒細璁＄鐩〃锛屽鐞嗚惀鏀瑰鍚庝細璁＄鐩皟鏁达紝鏇存柊鑷虫渶鏂扮◣鐜囥€?
2. 灏嗚彍鍗曡缃负"璐㈠姟"銆?
3. 琛ュ厖鍒嗙被鍙婃爣绛句俊鎭€?
4. 鏇存柊绋庨」淇℃伅锛屽鍔犱腑鍥藉父鐢ㄥ鍊肩◣鐜囪瀹氥€?
5. 鍙缃笂绾х鐩紝鏀寔浜岀骇绉戠洰銆傞厤鍚?app_web_widget_ztree"鍙鍔犳爲鐘跺鑸€?
6. 浣跨敤閲戣澏浼氳绉戠洰鍛藉悕娉曞澶氱骇绉戠洰鍒濆鍖栵紝浠ョ偣鍙峰垎闅斻€傚彲鑷璁惧畾绉戠洰浠ｇ爜銆?
7. 蹇呴』鍦ㄦ病鏈変笟鍔℃暟鎹€佹病鏈変細璁＄鐩殑鍒濆鐜瀹夎銆傚彲浣跨敤"app_odoo_customize"娓呴櫎璐㈠姟鏁版嵁閲嶇疆銆?
8. 鍖呭惈绉戠洰琛ㄦā鏉裤€佺鐩ā鏉裤€佺◣閲戞ā鏉裤€?
9. 澶氳瑷€鏀寔銆?
10. 澶氬叕鍙告敮鎸併€?
11. 鍏ㄧ増鏈敮鎸?Odoo 19,18,17,16,15,14,13,12锛屽吋瀹逛紒涓氱増鍜岀ぞ鍖虹増銆?
12. 浠ｇ爜瀹屽叏寮€婧愶紝鍩轰簬 LGPL-3 鍗忚銆?
    """,
    'depends': [
        'app_account_ztree',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'data/account_account_tag_data.xml',
        'views/account_account_views.xml',
        'report/account_report.xml',
        'report/report_voucher.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
