##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
##############################################################################

{
    'name': '网站博文超级搜索栏 / Website Blog Search Enhance Superbar',
    'version': '19.0.24.11.12',
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
        'website_blog',
        'app_base_superbar',
    ],
    'summary': '网站博文增强搜索，树状导航浏览博客文章 / Enhanced blog search with tree navigation for browsing posts',
    'description': """
1. Enhanced search for website blog posts.
2. Tree navigation for blog categories and tags.
3. Support list and kanban view for blog post browsing.
4. Multi-Language Support.
5. Multi-Company Support.
6. Full Version Support for Odoo 19,18,17,16,15,14,13,12, Enterprise and Community Edition.
7. Full Open Source under LGPL-3 license.
1. 网站博文增强搜索功能。
2. 博客分类和标签的树状导航。
3. 支持列表和看板视图浏览博文。
4. 多语言支持。
5. 多公司支持。
6. 全版本支持 Odoo 19,18,17,16,15,14,13,12，兼容企业版和社区版。
7. 代码完全开源，基于 LGPL-3 协议。
    """,
    'data': [
        'views/blog_post_views.xml',
        'views/ir_attachment_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
