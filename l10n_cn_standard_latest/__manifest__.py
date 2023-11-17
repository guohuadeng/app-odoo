# -*- coding: utf-8 -*-

# Copyright (C) 2008-2008 凯源吕鑫 lvxin@gmail.com   <basic chart data>
#                         维智众源 oldrev@gmail.com  <states data>
# Copyright (C) 2012-2012 南京盈通 ccdos@intoerp.com <small business chart>
# Copyright (C) 2008-now  开阖软件 jeff@osbzr.com    < PM and LTS >
# Copyright (C) 2017-now  jeffery9@gmail.com
# Copyright (C) 2018-11  欧度智能 https://www.odooai.cn

{
    'name': '2024最新中国会计科目表.企业标准会计.Latest Chinese Accounting for odoo16',
    'version': '23.09.18',
    'author': 'odooai.cn',
    'category': 'Accounting/Localizations/Account Charts',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 12,
    'summary': """    
    Multi level account chart. Chinese enhance. Focus on account chart.
    Add account chart group data. Account group, Chinese tax.
    Set chinese account report. 
    """,
    'description': """
    
    最新中国化财务，主要针对标准会计科目表作了优化。
    1. 2024最新会计科目表，处理营改增后会计科目调整。更新至最新税率。odoo 17专用。
    2. 将菜单中设置为"财务"。
    3. 补充分类及标签信息。
    4. 更新税信息。
    5. 增加树状结构，支持二级科目，可设置上级科目，配合 "app_web_superbar" 使用可轻易实现树状导航。
    6. 使用金蝶的会计科目命名法对多级科目进行初始化。可自行调整为用友科目命名法
    7. 注意，必须在没有业务数据，没有会计科目的初始环境。可以使用 "app_odoo_customize" 模块清除财务数据，重置会计科目。
     
    如果是多语种环境需要自行更改翻译，主要体现在3%,6%,13%增值税处理。
    中国财务，中国会计，中国城市
    欧度智能，odooai.cn
    The Latest Chinese Account
    Including the following data in the Accounting Standards for Business Enterprises
    包含企业会计准则以下数据
    
    * Chart of Accounts
    * 科目表模板
    * Account templates
    * 科目模板
    * Tax templates
    * 税金模板
    """,
    'depends': [
        'base',
        'account',
        'l10n_multilang',
        'app_odoo_customize',
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'views/account_account_views.xml',
        'views/account_views.xml',
        'data/chart_data.xml',
        'data/account_account_tag_data.xml',
        'data/account.group.csv',
        'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
