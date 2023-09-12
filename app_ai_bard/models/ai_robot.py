# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import requests, json
from odoo.exceptions import UserError
# todo: 暂时直接 requests
# from bardapi import Bard
import os

import logging

_logger = logging.getLogger(__name__)


class AiRobot(models.Model):
    _inherit = 'ai.robot'

    provider = fields.Selection(
        selection_add=[('google', 'Google Ai')],
        ondelete={'google': 'cascade'}
    ),
    set_ai_model = fields.Selection(
        selection_add=[('google-bard', 'Google Bard')],
        ondelete={'google-bard': 'cascade'})

    @api.onchange('provider')
    def _onchange_provider(self):
        if self.provider == 'google':
            self.endpoint = 'https://api.bard.ai/v1/text/generate'
        return super()._onchange_provider()
    
    def get_google(self, data, author_id, answer_id, param={}):
        self.ensure_one()
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.openapi_api_key}"}
        R_TIMEOUT = self.ai_timeout or 120
        o_url = self.endpoint or "https://api.bard.ai/v1/text/generate"
        
        # todo: 更多参数如 prompt, max_length
        max_tokens = param.get('max_tokens') if param.get('max_tokens') else self.max_tokens
        temperature = param.get('temperature') if param.get('temperature') else self.temperature
        pdata = {
            "text": data,
            "max_length": max_tokens,
            "temperature": temperature,
        }
        response = requests.post(o_url, data=json.dumps(pdata), headers=headers, timeout=R_TIMEOUT)
        response.raise_for_status()
        try:
            res = response.json()['text']
            return res
        except Exception as e:
            _logger.warning("Get Response Json failed: %s", e)
        else:
            _logger.warning('=====================Openai output data: %s' % response.json())
    
    def get_google_post(self, res, author_id=False, answer_id=False, param={}):
        if self.provider == 'google':
            content = res['text']
            return content, False, True
        
