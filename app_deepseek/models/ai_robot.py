# -*- coding: utf-8 -*-

import base64
import os
import requests, json
import logging
from openai import OpenAI
from http import HTTPStatus
from odoo import api, fields, models, modules, tools, _
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class AiRobot(models.Model):
    _inherit = 'ai.robot'

    provider = fields.Selection(selection_add=[('deepseek', 'Deepseek')], ondelete={'deepseek': 'set default'})
    set_ai_model = fields.Selection(
        selection_add=[
            ('deepseek-chat', 'Deepseek Chat'),
        ],
        ondelete={'deepseek-chat': 'set default'})

    @api.onchange('provider')
    def _onchange_provider(self):
        if self.provider == 'deepseek':
            if self.ai_model == 'deepseek-chat':
                self.endpoint = 'https://api.deepseek.com'
            # 取头像
            module_path = modules.get_module_path('app_ai', display_warning=False)
            if module_path:
                path = modules.check_resource_path(module_path, ('static/description/src/%s.png' % self.provider))
                if path:
                    image_file = tools.file_open(path, 'rb')
                    self.image_avatar = base64.b64encode(image_file.read())
        return super()._onchange_provider()

    def get_deepseek(self, data, author_id, answer_id, param={}):
        self.ensure_one()
        api_key = self.openapi_api_key
        if not api_key or not self.endpoint:
            raise UserError(_("Please provide Ai Robot [%s] API Key and Endpoint URL first." % self.name))

        if isinstance(data, list):
            messages = data
        else:
            messages = [{"role": "user", "content": data}]

        url = self.endpoint

        client = OpenAI(api_key=api_key, base_url=self.endpoint)
        response = client.chat.completions.create(
            model=self.ai_model,
            messages=messages
        )
        res = response.model_dump()
        if 'choices' in res:
            return res
        else:
            _logger.warning('=====================deepseek output data: %s' % response.json())

        return _("Response Timeout, please speak again.")

    def get_ai_post(self, res, author_id=False, answer_id=False, param={}):
        if self.provider == 'deepseek':
            usage = res['usage']
            content = res['choices'][0]['message']['content']
            return content, usage, True
        else:
            return super().get_ai_post(res, author_id, answer_id, param)

    def get_ai_list_model(self):
        self.ensure_one()
        if self.provider == 'deepseek':
            api_key = self.openapi_api_key
            if not api_key:
                raise UserError(_("Please provide Ai Robot [%s] API Key." % self.name))
            payload = {}
            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.openapi_api_key}'
            }
            R_TIMEOUT = self.ai_timeout or 120
            o_url = "https://api.deepseek.com/models"
            response = requests.get(o_url, headers=headers, data=payload, timeout=R_TIMEOUT)
            response.close()
            if response:
                res = response.json()
                r_text = json.dumps(res, indent=2)
            else:
                r_text = 'No response.'
            raise UserError(r_text)
        else:
            return super().get_ai_list_model()
