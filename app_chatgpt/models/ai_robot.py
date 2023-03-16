# -*- coding: utf-8 -*-

import requests
import openai
from odoo import api, fields, models, _


class AiRobot(models.Model):
    _name = 'ai.robot'
    _description = 'Gpt Robot'
    _order = 'sequence, name'

    name = fields.Char(string='Name', translate=True)
    provider = fields.Selection(string="AI Provider", selection=[('openai', 'OpenAI'), ('azure', 'Azure')], required=True, default='openai')
    ai_model = fields.Selection(string="AI Model", selection=[
        ('gpt-4', 'Chatgpt 4'),
        ('gpt-3.5-turbo', 'Chatgpt 3.5 Turbo'),
        ('gpt-3.5-turbo-0301', 'Chatgpt 3.5 Turbo on 20230301'),
        ('text-davinci-003', 'Chatgpt 3 Davinci'),
        ('code-davinci-002', 'Chatgpt 2 Code Optimized'),
        ('text-davinci-002', 'Chatgpt 2 Davinci'),
        ('dall-e2', 'Dall-E Image'),
    ], required=True, default='gpt-3.5-turbo',
                             help="""
GPT-3.5: A set of models that improve on GPT-3 and can understand as well as generate natural language or code
DALL·E: A model that can generate and edit images given a natural language prompt
Whisper: A model that can convert audio into text
Embeddings:	A set of models that can convert text into a numerical form
CodexLimited: A set of models that can understand and generate code, including translating natural language to code
Moderation: A fine-tuned model that can detect whether text may be sensitive or unsafe
GPT-3	A set of models that can understand and generate natural language
                             """)
    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here")
    temperature = fields.Float(string='Temperature', default=0.9)
    max_length = fields.Integer('Max Length', default=100)
    sequence = fields.Integer('Sequence', help="Determine the display order", default=10)

    def action_disconnect(self):
        requests.delete('https://chatgpt.com/v1/disconnect')

    def get_openai(self, data):
        openai.api_type = self.provider
        openai.api_base = "https://odooapp.openai.azure.com/"
        openai.api_version = "2022-12-01"
        openai.api_key = self.openapi_api_key
        response = openai.Completion.create(engine='odooapp', prompt=data, temperature=self.temperature, max_tokens=self.max_length, top_p=0.5, frequency_penalty=0,
                                            presence_penalty=0, stop=["Human:", "AI:"])
        if 'choices' in response:
            res = response['choices'][0]['text'].replace(' .', '.').strip()
            return res
