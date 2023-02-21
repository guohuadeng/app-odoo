# -*- coding: utf-8 -*-

# Created on 2023-02-016
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Copyright (c) 2020-Present InTechual Solutions. (<https://intechualsolutions.com/>)

{
    'name': 'ChatGPT Robot Multi Chat and Training(Under Construction)',
    'version': '16.23.02.20',
    'author': 'Sunpop.cn',
    'company': 'Sunpop.cn',
    'maintainer': 'Sunpop.cn',
    'category': 'Website/Website',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'license': 'AGPL-3',
    'images': ['static/description/banner.png'],
    'summary': '''
    Multi Odoo ChatGPT Robot. Integration All ChatGpt Api.
    Chat channel with several ChatGPT Robots.
    Whitelist and blacklist for Users or IP.
    Base on is_chatgpt_integration from InTechual Solutions.
    ''',
    'description': '''
    Allows the application to leverage the capabilities of the GPT language model to generate human-like responses,
    providing a more natural and intuitive user experience.
    1. Multi ChatGpt robot Connector. Chat and train.
    2. Multi User Chat with ChatGpt
    3. ChatGpt Channel for Group Chat
    4. White and black List for ChatGpt
    5. Demo Chat time for new user
    6. Easy Start and Stop ChatGpt
    ''',
    'depends': ['base', 'base_setup', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_channel_data.xml',
        'data/gpt_robot_data.xml',
        'data/user_partner_data.xml',
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
        'views/gpt_robot_views.xml',
        'views/res_users_views.xml',
    ],
    'assets': {
        'mail.assets_messaging': [
            'app_chatgpt/static/src/models/*.js',
        ],
        'mail.assets_model_data': [
            'app_chatgpt/static/src/models_data/*.js',
        ],
    },
    'external_dependencies': {'python': ['openai']},
    'installable': True,
    'application': False,
    'auto_install': False,
}
