##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
##############################################################################

{
    'name': '电商产品源码编辑器 / Website Product SEO &amp; Source Code Editor',
    'version': '18.0.25.10.31',
    'author': 'odooai.cn',
    'category': 'Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'depends': [
        'website_sale',
    ],
    'summary': '源码方式编辑电商产品页面，批量SEO优化 / Edit e-commerce product page in source code mode with mass SEO',
    'description': """
1. Edit website product page in source code mode. Edit product category page.
2. Mass edit website product page SEO like title, description, keyword.
3. Mass translate website page, blog and product to any language (requires app_ai_seo).
4. Easy mass SEO builder with AI editing capabilities (requires app_ai_seo).
5. Multi-Language Support.
6. Multi-Company Support.
7. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
8. Full Open Source under LGPL-3 license.
1. 源码方式编辑电商产品页面和产品分类页面。
2. 批量编辑产品页面 SEO，如标题、描述、关键词。
3. 批量翻译网站页面、博客和产品信息到任意语言（需要 app_ai_seo）。
4. 批量 SEO 构建，使用 AI 编辑和优化网站（需要 app_ai_seo）。
5. 多语言支持。
6. 多公司支持。
7. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
8. 代码完全开源，基于 LGPL-3 协议。
    """,
    'data': [
        'views/product_template_views.xml',
        'views/product_public_category_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
