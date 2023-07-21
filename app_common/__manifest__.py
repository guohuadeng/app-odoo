# -*- coding: utf-8 -*-

# Created on 20120-01-05
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo12在线用户手册（长期更新）
# https://www.odooai.cn/documentation/user/12.0/zh_CN/index.html

# Odoo12在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/12.0/index.html

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
    'name': "odooai Odooapp Common Func",
    'version': '12.22.08.21',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Core for common use odooai apps.
    基础核心，必须没有要被依赖字段及视图等，实现auto_install
    ''',
    'description': '''    
    Support Odoo 13，12, Enterprise and Community Edition
    1. Base function add timezone convert
    2. Remove select add warning
    3. Cron add user log
    4. Rng file add extra function
    5. User add index
    6. Add bg-xxx class like bg-danger
    7. Add ali iconfont support, more icon
    11. Multi-language Support.
    12. Multi-Company Support.
    13. Support Odoo 13，12, Enterprise and Community Edition
    ==========
    1. 
    2. 
    3. 多语言支持
    4. 多公司支持
    5. Odoo 13, 12, 企业版，社区版，多版本支持
    ''',
    'depends': [
        'web',
    ],
    'data': [
        # 'security/*.xml',
        # 'security/ir.model.access.csv',
        # 'data/.xml',
        'views/ir_cron_views.xml',
        'views/webclient_templates.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
