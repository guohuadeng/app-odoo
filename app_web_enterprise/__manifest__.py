{
    'name': 'Odoo 浼佷笟鐗堢晫闈㈠寮?/ Enterprise UI Enhance Pack',
    'version': '19.0.26.08.29',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '浼佷笟鐗堢晫闈㈠寮哄浠讹紝鎶ょ溂缁胯壊涓昏壊銆佽彍鍗曠澶淬€佸瓧娈典笅鍒掔嚎銆佽〃鏍煎垎闅旂嚎 / Enterprise UI enhance with green theme, menu arrows, field underline and grid lines',
    'description': """
1. UI Enhance pack of Odoo Enterprise version with comfortable green color.
2. Add dropdown arrow to parent menu group for easier navigation.
3. Replace the Odoo logo or URL to your company logo in menu and page.
4. Add underline for editable input fields for better visibility.
5. Add grid lines to list view for easier data reading.
6. Add grid lines to Account Reports for easier data viewing and reconciliation.
7. Support dark mode theme.
8. Optimize one2many list empty row strategy: compact layout with only 1 filler row when no data.
9. Multi-Language Support.
10. Multi-Company Support.
11. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
12. Full Open Source under LGPL-3 license.
13. Fix Odoo core Popover TypeError: Cannot read properties of undefined (reading 'contains'), caused by stale pointerdown listener after Popover target destruction.
1. Odoo 浼佷笟鐗堢晫闈㈠寮哄浠讹紝浣跨敤鏇磋垝閫傛姢鐪肩殑缁胯壊浣滀负涓昏壊銆?
2. 澶氱骇鑿滃崟涓嚭鐜颁笅鎷夌澶达紝瀵艰埅鎿嶄綔鏇存柟渚裤€?
3. 鏇挎崲涓昏彍鍗曠晫闈㈢殑 Logo 涓哄叕鍙?Logo銆?
4. 鍦ㄥ彲缂栬緫瀛楁涓嬫柟澧炲姞涓嬪垝绾匡紝鏄撲簬鍒嗚鲸銆?
5. 涓鸿〃鏍煎垪琛ㄥ鍔犺鍒楀垎闅旂嚎锛屾槗浜庣湅鏁版嵁銆?
6. 涓鸿储鍔℃姤琛ㄥ鍔犺鍒楀垎闅旂嚎锛屾槗浜庣湅鏁版嵁鍙婂璐︺€?
7. 鏀寔榛戝妯″紡涓婚銆?
8. 浼樺寲 One2Many 鍒楄〃绌鸿濉厖绛栫暐锛氫粎鏃犳暟鎹椂琛ュ厖 1 涓┖琛岋紝鏈夋暟鎹椂涓嶈ˉ鍏咃紝鐣岄潰鏇寸揣鍑戙€?
9. 澶氳瑷€鏀寔銆?
10. 澶氬叕鍙告敮鎸併€?
11. 鍏ㄧ増鏈敮鎸?Odoo 19,18,17,16,15,14,13,12锛屽吋瀹逛紒涓氱増鍜岀ぞ鍖虹増銆?
12. 浠ｇ爜瀹屽叏寮€婧愶紝鍩轰簬 LGPL-3 鍗忚銆?
13. 淇 Odoo 鍘熺敓 Popover TypeError: Cannot read properties of undefined (reading 'contains')锛屽洜 Popover target 閿€姣佸悗 window pointerdown 鐩戝惉鍣ㄦ湭鍙婃椂娓呯悊瀵艰嚧銆?
    """,
    'price': 68.00,
    'currency': 'EUR',
    'depends': [
        'app_odoo_customize',
        'web_enterprise',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('before', 'web_enterprise/static/src/scss/primary_variables.scss', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            ('before', 'web_enterprise/static/src/webclient/home_menu/home_menu.variables.scss', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
            ('before', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_before.scss'),
            ('after', 'web/static/src/views/**/*', 'app_web_enterprise/static/src/scss/app_style_after.scss'),
            ('after', 'web_enterprise/static/src/webclient/navbar/navbar.variables.scss', 'app_web_enterprise/static/src/webclient/navbar.variables.scss'),
            ('after', 'web_enterprise/static/src/webclient/navbar/navbar.scss', 'app_web_enterprise/static/src/webclient/navbar.scss'),
            'app_web_enterprise/static/src/webclient/**/*.xml',
            'app_web_enterprise/static/src/xml/res_config_edition.xml',
            'app_web_enterprise/static/src/js/list_renderer.js',
            'app_web_enterprise/static/src/js/popover_fix.js',
        ],
        'web.dark_mode_variables': [
            ('remove', 'app_web_enterprise/static/src/scss/primary_variables.scss'),
            ('before', 'web_enterprise/static/src/scss/primary_variables.dark.scss', 'app_web_enterprise/static/src/scss/primary_variables.dark.scss'),
        ],
        'web.assets_web_dark': [
            ('remove', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
            ('remove', 'app_web_enterprise/static/src/webclient/navbar.variables.scss'),
            ('remove', 'app_web_enterprise/static/src/webclient/navbar.scss'),
        ],
        'website.assets_editor': [
            'app_web_enterprise/static/src/scss/app_style_website_editor.scss',
        ],
        'web.assets_frontend': [
            ('before', 'web_enterprise/static/src/webclient/home_menu/home_menu.variables.scss', 'app_web_enterprise/static/src/scss/home_menu.variables.scss'),
            'app_web_enterprise/static/src/scss/app_style_website.scss',
        ],
    },
    'images': ['static/description/app_web_enterprise_03.jpg'],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': True,
}
