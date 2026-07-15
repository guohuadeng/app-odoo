{
    'name': 'Odoo 企业版界面增强 / Enterprise UI Enhance Pack',
    'version': '18.0.26.07.16',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '企业版界面增强套件，护眼绿色主色、菜单箭头、字段下划线、表格分隔线 / Enterprise UI enhance with green theme, menu arrows, field underline and grid lines',
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
1. Odoo 企业版界面增强套件，使用更舒适护眼的绿色作为主色。
2. 多级菜单中出现下拉箭头，导航操作更方便。
3. 替换主菜单界面的 Logo 为公司 Logo。
4. 在可编辑字段下方增加下划线，易于分辨。
5. 为表格列表增加行列分隔线，易于看数据。
6. 为财务报表增加行列分隔线，易于看数据及对账。
7. 支持黑夜模式主题。
8. 优化 One2Many 列表空行填充策略：仅无数据时补充 1 个空行，有数据时不补充，界面更紧凑。
9. 多语言支持。
10. 多公司支持。
11. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
12. 代码完全开源，基于 LGPL-3 协议。
13. 修复 Odoo 原生 Popover TypeError: Cannot read properties of undefined (reading 'contains')，因 Popover target 销毁后 window pointerdown 监听器未及时清理导致。
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
