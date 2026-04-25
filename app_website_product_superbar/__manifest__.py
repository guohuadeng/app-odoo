{
    'name': '网站产品按分类超级搜索栏 / Website Product Browse by Category Superbar',
    'version': '18.0.24.11.12',
    'author': 'odooai.cn',
    'category': 'Extra tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': '按网站产品分类树状导航浏览产品 / Browse website products by category tree with parent children navigator',
    'description': """
1. Browse website products by category tree with parent children navigator.
2. Advance search with real parent children tree in ListView, KanbanView, Pivot and Graph view.
3. Support search more view for quick product lookup.
4. Easy to customize for any Odoo module.
5. Multi-Language Support.
6. Multi-Company Support.
7. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
8. Full Open Source under LGPL-3 license.
1. 按网站产品分类树状导航浏览产品。
2. 使用父子树结构在列表、看板、透视和图表视图中进行高级搜索。
3. 支持搜索更多视图，快速查找产品。
4. 易于定制，可在 Odoo 任何模块中使用。
5. 多语言支持。
6. 多公司支持。
7. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
8. 代码完全开源，基于 LGPL-3 协议。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'website_sale',
        'app_product_superbar',
    ],
    'images': ['static/description/banner.png', 'static/description/product1.jpg'],
    'data': [
        'views/product_template_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
