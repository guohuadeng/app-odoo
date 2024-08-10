# -*- coding: utf-8 -*-

# Created on 2022-09-01
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# Odoo13在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/13.0/zh_CN/index.html

# Odoo13在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/13.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "Website Product Editor source code,SEO Editor.Odoo电商产品源码编辑器",
    'version': '24.04.01',
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
    'summary': '''
    Edit odoo Product website description in source code.Make developer to easy build website.
    Quick seo website product sale page. mass edit page and blog. Website Product SEO editor.
    ''',
    'description': '''
    Make developer to easy build e-commerce website.
    1. Edit website product page in source code mode. Edit Product Category Page.
    2. Mass edit website product page seo like title, description, keyword etc..
    3. Mass translate website page, website blog, website product to any language. this need extra pay for app_ai_seo
    4. Easy mass seo builder. Use AI to edit website. mass setup seo. this need extra pay for app_ai_seo
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ==========
    程序员电商网站开发专用
    1. 快速电商产品页编辑，源码方式编辑网站产品内容
    2. 批量产品网页内容编辑
    3. 批量翻译网站页面，博客，产品信息。快速生成全球化网站，需要额外付费模块 app_ai_seo
    4. 批量SEO，提升网站排名。使用Ai编辑及优化网站，需要额外付费模块 app_ai_seo
    11. 多语言支持，多公司支持
    12. Odoo 17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
    ''',
    'data': [
        'views/product_template_views.xml',
        'views/product_public_category_views.xml',
        # 'report/.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
