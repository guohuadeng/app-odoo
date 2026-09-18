# -*- coding: utf-8 -*-

# Created on 2026-09-12
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Claude AI集成 / Claude AI for Odoo AI Center',
    'version': '18.0.26.09.12',
    'author': 'odooai.cn',
    'company': 'odooai.cn',
    'maintainer': 'odooai.cn',
    'category': 'Website/Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Claude AI for Odoo AI Center. Ai Aigc Center including Claude, Deepseek, Azure Chatgpt Ai, OpenAi Chatgpt Ai.
    Ai服务中心的Claude支持，包括Claude Opus 4.1、Claude Sonnet 4.5、Claude Haiku等模型，本版本支持对话模型。
    Integration All Ai robot Api, like Anthropic Claude Messages Api.
    Easy Chat channel with several Ai Robots and train.
    ''',
    'description': '''
English Features:
1. Chat with Claude AI (Anthropic) in Odoo, leveraging Claude language model for human-like responses.
2. Multi Claude robot connector with chat and training capabilities.
3. Support Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4.5, Claude Sonnet 4, Claude 3.7 Sonnet, Claude 3.5 Sonnet, Claude 3.5 Haiku, Claude 3 Opus, Claude 3 Haiku models.
4. Native Anthropic Messages API integration with system prompt and vision (image) message support.
5. Bind Claude API to user for robot chat or group channel conversation.
6. White and black list management for AI access control.
7. Easy start and stop Claude service.
8. Evaluate AI robot responses to improve quality through training.
9. Synchronous or Asynchronous mode for AI response.
10. Sensitive words filter setup.
11. Multi-language Support. Multi-Company Support.
12. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
13. Full Open Source.

中文功能：
1. 在Odoo中与Claude AI（Anthropic）对话，利用Claude语言模型生成自然流畅的回复。
2. 多Claude机器人连接器，支持聊天与训练。
3. 支持Claude Opus 4.1、Claude Opus 4、Claude Sonnet 4.5、Claude Sonnet 4、Claude 3.7 Sonnet、Claude 3.5 Sonnet、Claude 3.5 Haiku、Claude 3 Opus、Claude 3 Haiku模型。
4. 原生Anthropic Messages API对接，支持系统提示词与图片消息。
5. 将Claude API绑定到用户，支持机器人私聊或群聊频道。
6. AI白名单和黑名单管理。
7. 轻松启动和停止Claude服务。
8. 评估AI机器人回复质量，通过训练持续改进。
9. 支持同步或异步模式获取AI回复。
10. 敏感词过滤设置。
11. 多语言支持。多公司支持。
12. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
13. 代码完全开源。
    ''',
    'depends': [
        'app_chatgpt',
    ],
    'data': [
        'data/ai_robot_data.xml',
        'data/user_partner_data.xml',
        'data/discuss_channel_data.xml',
        'views/ai_robot_views.xml',
    ],
    'assets': {
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
