# -*- coding: utf-8 -*-

# Created on 2023-09-15
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': '深度求索AI集成 / Deepseek AI for Odoo AI Center',
    'version': '19.0.25.02.10',
    'author': 'odooai.cn',
    'company': 'odooai.cn',
    'maintainer': 'odooai.cn',
    'category': 'Website/Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'license': 'LGPL-3',
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Deepseek AI for Odoo AI Center. Ai Aigc Center including Deepseek, Azure Chatgpt Ai, OpenAi Chatgpt Ai.
    Ai服务中心的DeepSeek支持，包括V3和R1等，本版本只支持开放对话模型。
    Integration All Ai robot Api, like Azure OpenAI Chatgpt Service.
    Also support(need extra pay) Ali Ai, Baidu Ai, Kimi Ai.
    Easy Chat channel with several Ai Robots and train.
    ''',
    'description': '''
English Features:
1. Chat with Deepseek AI in Odoo, leveraging GPT-like language model for human-like responses.
2. Multi ChatGPT OpenAI robot connector with chat and training capabilities.
3. Multi AI support including Google Bard AI, Azure AI, ChatGPT 4, ChatGPT 3.5 Turbo, ChatGPT 3 Davinci, ChatGPT 2 Code Optimized, Dall-E Image.
4. Bind ChatGPT API to user for robot chat or group channel conversation.
5. White and black list management for ChatGPT access control.
6. Setup demo chat time for every new user.
7. Easy start and stop ChatGpt service.
8. Evaluate AI robot responses to improve quality through training.
9. Microsoft Azure OpenAI Service API support.
10. Synchronous or Asynchronous mode for AI response.
11. Sensitive words filter setup.
12. Multi-language Support. Multi-Company Support.
13. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
14. Full Open Source.

中文功能：
1. 在Odoo中与Deepseek AI对话，利用类GPT语言模型生成自然流畅的回复。
2. 多ChatGPT OpenAI机器人连接器，支持聊天与训练。
3. 多AI平台支持，包括Google Bard AI、Azure AI、ChatGPT 4、ChatGPT 3.5 Turbo、ChatGPT 3 Davinci、ChatGPT 2 Code Optimized、Dall-E图像。
4. 将ChatGPT API绑定到用户，支持机器人私聊或群聊频道。
5. ChatGPT白名单和黑名单管理。
6. 为新用户设置演示聊天时长。
7. 轻松启动和停止ChatGPT服务。
8. 评估AI机器人回复质量，通过训练持续改进。
9. Microsoft Azure OpenAI服务API对接支持。
10. 支持同步或异步模式获取AI回复。
11. 敏感词过滤设置。
12. 多语言支持。多公司支持。
13. 支持Odoo 19,18,17,16,15,14,13,12，企业版、社区版及odoo.sh。
14. 代码完全开源。
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
