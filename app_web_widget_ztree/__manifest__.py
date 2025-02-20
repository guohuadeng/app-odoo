# -*- coding: utf-8 -*-

# Created on 2021-11-30
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# change ztree to  https://github.com/wenzhixin/font-awesome-zTree

{
    'name': 'Many2One Hierarchy Parent Child M2o Selector, zTree 树状下拉选择器',
    'version': '17.0.24.12.18',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'OPL-1',
    'sequence': 2,
    'summary': """
    show parent tree, parent children node in m2o select field.
    Use for parent children tree list select navigator.
    ztree widget.
    """,
    'description': """
    zTree widget.
    Advance search with real parent children tree, ListView or KanbanView ,
    eg: Product category tree ,Department tree, stock location tree.
M2O字段下拉树状选择器，Many2One动态父子多层级关系树展现widget小组件，可用于任何模块。
用于父子树列表选择导航器。例如品类，部门等多层次展现。
已内置10多个免费odoo应用的多层级选择，如产品，Hr部门，联系人，仓库货架等。
    1. M2o Select with Hierarchy parent/child dropdown.
    2. zTree widget for any app in odoo.
    3. Easy use in customize 3rd app. Easy to make custom parent children tree.
    4. Hierarchy selector out-of-box with all apps:
    Product, Sales, Purchase, MRP, Stock, Etc...
    5. zTree树状下拉选择器，可完全自定义的Widget
    """,
    'price': 108.00,
    'currency': 'EUR',
    'depends': [
        'web',
        # 'product',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        # 'views/product_views.xml',
    ],
    'assets': {
        'web.assets_qweb': [
        ],
        'web.assets_backend': [
            'app_web_widget_ztree/static/src/lib/ztree_v3/css/awesomeStyle/fa.scss',
            'app_web_widget_ztree/static/src/lib/ztree_v3/css/awesomeStyle/awesome.scss',
            'app_web_widget_ztree/static/src/scss/variables.scss',
            'app_web_widget_ztree/static/src/scss/views.scss',
            'app_web_widget_ztree/static/src/lib/ztree_v3/js/jquery.ztree.core.js',
            ('after', 'web/static/src/core/autocomplete/autocomplete.js', 'app_web_widget_ztree/static/src/js/ztree.js'),
            ('after', 'web/static/src/views/fields/x2many/x2many_field.js', 'app_web_widget_ztree/static/src/js/ztree_chart.js'),
            ('after', 'web/static/src/views/fields/relational_utils.js', 'app_web_widget_ztree/static/src/js/ztree_many2x.js'),
            ('after', 'web/static/src/views/fields/many2one/many2one_field.js', 'app_web_widget_ztree/static/src/js/ztree_select.js'),
            ('after', 'web/static/src/core/autocomplete/autocomplete.xml', 'app_web_widget_ztree/static/src/xml/ztree.xml'),
            'app_web_widget_ztree/static/src/xml/ztree_chart.xml',
            ('after', 'web/static/src/views/fields/relational_utils.xml', 'app_web_widget_ztree/static/src/xml/ztree_many2x.xml'),
            ('after', 'web/static/src/views/fields/many2one/many2one_field.xml', 'app_web_widget_ztree/static/src/xml/ztree_select.xml'),
        ],
    },
    'demo': [
    ],
    'test': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}

