# -*- coding: utf-8 -*-

# Created on 2023-02-016
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Copyright (c) 2020-Present InTechual Solutions. (<https://intechualsolutions.com/>)

{
    'name': "AI服务中心聚合全网AI,ChatGPT DeepSeek Ali Qwen AiGC Center",
    'version': '18.0.26.03.26',
    'author': 'odooai.cn',
    'company': 'odooai.cn',
    'maintainer': 'odooai.cn',
    'category': 'Website/Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'summary': "Odoo AI中心，集成ChatGPT4、DeepSeek、阿里通义千问、百度文心等多种AI。Multi AI integration with ChatGPT4, DeepSeek, Ali Qwen, Baidu in Odoo AI Center.",
    'description': '''
    1. Multi ChatGPT OpenAI robot connector. Chat and train.
    2. Multi AI support: ChatGPT-4o, GPT-4 32k, GPT-3.5 Turbo, GPT-3 Davinci, Azure AI, Alibaba Qwen AI, Baidu AI, DeepSeek.
    3. Bind AI robot to user for private chat or AI channel for group chat.
    4. White and black list for AI access control.
    5. Setup demo chat time for every new user.
    6. Easy start and stop AI robots.
    7. Evaluation AI responses for training improvement.
    8. Connect Microsoft Azure OpenAI Service.
    9. Synchronous or asynchronous mode for AI response.
    10. Sensitive words filter.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.

    To install: pip install openai==1.59.5 && pip3 install typing-extensions==4.12.2

    1. 多ChatGPT OpenAI机器人连接器，支持对话与训练
    2. 多AI支持：ChatGPT-4o、GPT-4 32k、GPT-3.5 Turbo、GPT-3 Davinci、Azure AI、阿里通义千问、百度文心、DeepSeek
    3. 将AI机器人绑定到用户进行私聊或群聊频道
    4. AI访问黑白名单控制
    5. 为新用户设置体验对话时间
    6. 轻松启动和停止AI机器人
    7. 评价AI回复质量持续优化训练
    8. 连接Microsoft Azure OpenAI服务
    9. 支持同步或异步AI响应模式
    10. 敏感词过滤
    11. 多语言支持，多公司支持
    12. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    13. 代码完全开源
    ''',
    'depends': [
        'app_odoo_customize',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'data/discuss_channel_data.xml',
        'data/ai_robot_data.xml',
        'data/user_partner_data.xml',
        'data/ir_config_parameter.xml',
        'views/ai_robot_views.xml',
        'views/res_partner_ai_use_views.xml',
        'views/res_users_views.xml',
        'views/discuss_channel_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_chatgpt/static/src/models/message_model.js',
            'app_chatgpt/static/src/components/message/message.js',
            'app_chatgpt/static/src/components/*/*.xml',
        ],
    },
    'external_dependencies': {'python': ['typing_extensions', 'openai']},
    'installable': True,
    'application': True,
    'auto_install': False,
}
