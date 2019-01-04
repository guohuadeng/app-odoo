# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12在线用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# http://www.sunpop.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/

# Odoo, Open Source Web Widget Color
# Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# Copyright (C) 2014 Anybox <http://anybox.fr>
# Copyright (C) 2015 Taktik SA <http://taktik.be>
# Copyright (C) 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "App Product Attribute Color",
    'category': "Sales",
    'version': "12.19.1.04",
    "author": "Sunpop.cn",
    'price': 0.00,
    'currency': 'EUR',
    'summary': """
    Use for quick select color. can be use in product attribute and other color variant. color widget. color pick.
    """,
    'depends': [
        'app_web_widget_color',
        'sale',
    ],
    'data': [
        'view/product_attribute_views.xml'
    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
    'license': 'AGPL-3',
    'auto_install': True,
    'installable': True,
}
