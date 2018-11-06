# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:


{
    'name': "App account Chinese，最新中国标准会计科目，会计增强",
    'version': '11.0.11.06',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'http://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': """    
    Chinese enhance. Focus on account.
    update tax.
    add account chart group data.
    Set account group.
    Set chinese tax.
    Set chinese account report. 
    """,
    'description': """
    中国化财务，主要针对标准会计科目表。
    中国会计科目表 （财会[2017]14号《企业会计准则》
    注意，如果是多语种环境需要自行更改翻译，主要体现在16%增值税处理。
    广州尚鹏，Sunpop.cn
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        "account",
        "account_asset",
        "account_accountant",
        "l10n_cn_standard",
    ],
    'images': [],
    'data': [
        'views/account_account_views.xml',
        'views/account_views.xml',
        'data/account.group.csv',
        'data/account_tax_template_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': True,
}
