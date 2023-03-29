# -*- coding: utf-8 -*-

import requests
import openai
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from .lib.WordsSearch import WordsSearch

import logging
_logger = logging.getLogger(__name__)


class AiRobot(models.Model):
    _name = 'ai.robot'
    _description = 'Gpt Robot'
    _order = 'sequence, name'

    name = fields.Char(string='Name', translate=True, required=True)
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
GPT-4: Can understand Image, generate natural language or code.
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
    max_length = fields.Integer('Max Length', default=300)
    endpoint = fields.Char('End Point', default='https://api.openai.com/v1/chat/completions')
    engine = fields.Char('Engine', help='If use Azure, Please input the Model deployment name.')
    api_version = fields.Char('API Version', default='2022-12-01')
    sequence = fields.Integer('Sequence', help="Determine the display order", default=10)
    sensitive_words = fields.Text('Sensitive Words', help='Sensitive word filtering. Separate keywords with a carriage return.')
    is_filtering = fields.Boolean('Filter Sensitive Words', default=False)

    def action_disconnect(self):
        requests.delete('https://chatgpt.com/v1/disconnect')

    def get_openai(self, data):
        self.ensure_one()
        # only for azure
        openai.api_type = self.provider
        if not self.endpoint:
            raise UserError(_("Please Set your AI robot's endpoint first."))
        openai.api_base = self.endpoint
        if not self.api_version:
            raise UserError(_("Please Set your AI robot's API Version first."))
        openai.api_version = self.api_version
        openai.api_key = self.openapi_api_key
        response = openai.Completion.create(
            engine=self.engine,
            prompt=data,
            temperature=self.temperature or 0.9,
            max_tokens=self.max_length or 600,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0, stop=["Human:", "AI:"])

        _logger.warning('=====================azure input data: %s' % data)
        if 'choices' in response:
            res = response['choices'][0]['text'].replace(' .', '.').strip()
            res = self.filter_sensitive_words(res)
            return res

    @api.onchange('provider')
    def _onchange_provider(self):
        if self.provider == 'openai':
            self.endpoint = 'https://api.openai.com/v1/chat/completions'
        elif self.provider == 'azure':
            self.endpoint = 'https://odoo.openai.azure.com'
            
    def filter_sensitive_words(self, data):
        if self.is_filtering:
            search = WordsSearch()
            s = self.sensitive_words
            search.SetKeywords(s.split('\n'))
            result = search.Replace(text=data)
            return result
