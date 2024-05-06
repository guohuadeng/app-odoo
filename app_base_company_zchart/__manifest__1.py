# -*- coding: utf-8 -*-

# Created on 2019-01-04
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


{
    'name': 'Group Company Multi Level Chart Hierarchy, 集团公司多层级结构图zChart',
    'version': '16.24.05.06',
    'author': 'odooai.cn',
    'category': 'Sales',
    'website': 'https://www.odooai.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Group Company Chart Hierarchy with zchart Widget. Hierarchy Chart, Hierarchy Tree for multi level Parent Children relation tree.
    Free for Multi company Hierarchy chart category Hierarchy chart, stock Hierarchy chart. account chart. user multi level chart.
    """,
    'description': """    
Need extra paid apps https://www.odoo.com/apps/modules/16.0/app_web_widget_ztree/
This module extend to show a Hierarchy chart.
(N+1, N+2, direct subordinates)
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'base',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        # 'security/res_group.xml',
        # 'views/res_company_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

