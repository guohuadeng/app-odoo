# -*- coding: utf-8 -*-

# Created on 2023-02-016
# author: 娆у害鏅鸿兘锛宧ttps://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': '璋锋瓕Gemini AI鏀寔,Google Gemini (Bard) AI for Odoo',
    'version': '19.0.25.07.26',
    'author': 'odooai.cn',
    'company': 'odooai.cn',
    'maintainer': 'odooai.cn',
    'category': 'Website/Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'images': ['static/description/banner.gif', 'static/description/banner.png'],
    'summary': "Odoo AI涓績闆嗘垚Google Gemini(Bard)AI锛屾敮鎸佸AI鏈哄櫒浜哄璇濅笌璁粌銆侴oogle Gemini AI integration for Odoo AI Center with multi-robot chat and training.",
    'description': '''
    Chat with google Gemini ai with odoo.
    Allows the application to leverage the capabilities of the GPT language model to generate human-like responses,
    providing a more natural and intuitive user experience.
    odoo bard connector.
    1. Multi ChatGpt openAI robot Connector. Chat and train.
    2. Multi Ai support including Google Bard Ai, Azure Ai, Chatgpt 4, Chatgpt 3.5 Turbo, Chatgpt 3 Davinci, Chatgpt 2 Code Optimized, 'Dall-E Image.
    3. Bind ChatGpt Api to user. So we can chat to robot user or use ChatGpt Channel for Group Chat.
    4. White and black List for ChatGpt.
    5. Setup Demo Chat time for every new user.
    6. Easy Start and Stop ChatGpt.
    7. Evaluation the ai robot to make better response. This training.
    8. Add api support Connect the Microsoft Azure OpenAI Service.
    9. Can set Synchronous or Asynchronous mode for Ai response.
    10.Filter Sensitive Words Setup.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ''',
    'depends': [
        'app_chatgpt',
    ],
    'data': [
        # 'data/ai_provider_data.xml',
        'data/ai_robot_data.xml',
        'data/user_partner_data.xml',
    ],
    'assets': {
    },
    'external_dependencies': {'python': ['bardapi']},
    'installable': True,
    'application': True,
    'auto_install': False,
}
