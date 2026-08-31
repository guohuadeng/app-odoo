{
    'name': '表单全宽度满屏 / Web Form Fullwidth &amp; Chatter Position',
    'version': '19.0.25.04.05',
    'category': 'Extra tools',
    'author': 'odooai.cn',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 18.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '表单全屏全宽显示，自定义备注消息位置 / Form responsive full screen with configurable chatter position',
    'description': """
1. Form view fullwidth and full screen for better use of screen space.
2. Easy config the chatter position to bottom, side or responsive per user.
3. Easy set all company user UI for chatter position globally.
4. Ready for small, medium, large and extra large screens.
5. Ready for enterprise and community edition.
6. Multi-Language Support.
7. Multi-Company Support.
8. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
9. Full Open Source under LGPL-3 license.
1. 表单视图全屏全宽显示，更好利用屏幕空间。
2. 可为每个用户配置备注消息（Chatter）位置：底部、侧边或响应式。
3. 可全局设置所有公司用户的备注消息位置。
4. 适配小、中、大、超大屏幕尺寸。
5. 兼容企业版和社区版。
6. 多语言支持。
7. 多公司支持。
8. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
9. 代码完全开源，基于 LGPL-3 协议。
    """,
    'depends': [
        'app_common'
    ],
    'data': [
        'views/res_users_views.xml',
        'views/res_config_settings_views.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ('after', 'web/static/src/views/**/*', 'app_web_fullwidth/static/src/scss/app_style_after.scss'),
            '/app_web_fullwidth/static/src/js/form_compiler.js'
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
