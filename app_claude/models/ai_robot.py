# -*- coding: utf-8 -*-

# Created on 2026-09-12
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import re
import requests, json
import logging
from odoo import api, fields, models, modules, tools, _
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)

# Anthropic Messages API 版本与默认接入点
ANTHROPIC_API_VERSION = '2023-06-01'
CLAUDE_DEFAULT_ENDPOINT = 'https://api.anthropic.com/v1/messages'
CLAUDE_MODELS_URL = 'https://api.anthropic.com/v1/models'


class AiRobot(models.Model):
    _inherit = 'ai.robot'

    provider = fields.Selection(
        selection_add=[('claude', 'Claude (Anthropic)')],
        ondelete={'claude': 'set default'})
    set_ai_model = fields.Selection(
        selection_add=[
            ('claude-opus-4-1', 'Claude Opus 4.1'),
            ('claude-opus-4-0', 'Claude Opus 4'),
            ('claude-sonnet-4-5', 'Claude Sonnet 4.5'),
            ('claude-sonnet-4-0', 'Claude Sonnet 4'),
            ('claude-3-7-sonnet-latest', 'Claude 3.7 Sonnet'),
            ('claude-3-5-sonnet-latest', 'Claude 3.5 Sonnet'),
            ('claude-3-5-haiku-latest', 'Claude 3.5 Haiku'),
            ('claude-3-opus-latest', 'Claude 3 Opus'),
            ('claude-3-haiku-20240307', 'Claude 3 Haiku'),
        ],
        ondelete={
            'claude-opus-4-1': 'set default',
            'claude-opus-4-0': 'set default',
            'claude-sonnet-4-5': 'set default',
            'claude-sonnet-4-0': 'set default',
            'claude-3-7-sonnet-latest': 'set default',
            'claude-3-5-sonnet-latest': 'set default',
            'claude-3-5-haiku-latest': 'set default',
            'claude-3-opus-latest': 'set default',
            'claude-3-haiku-20240307': 'set default',
        })

    @api.onchange('provider')
    def _onchange_provider(self):
        if self.provider == 'claude':
            self.endpoint = CLAUDE_DEFAULT_ENDPOINT
            # 取头像
            module_path = modules.get_module_path('app_claude', display_warning=False)
            if module_path:
                path = modules.check_resource_path(module_path, ('static/src/img/%s.png' % self.provider))
                if path:
                    image_file = tools.file_open(path, 'rb')
                    self.image_avatar = base64.b64encode(image_file.read())
        return super()._onchange_provider()

    def _claude_headers(self):
        # Anthropic Messages API 认证头
        return {
            'x-api-key': self.openapi_api_key,
            'anthropic-version': ANTHROPIC_API_VERSION,
            'content-type': 'application/json',
        }

    def _claude_convert_messages(self, messages):
        # openai 风格消息转 claude 风格：
        # 1. system 提示词抽出，claude 要求顶层传
        # 2. openai 图片 data uri 转 claude base64 source
        system_parts = []
        out = []
        for msg in messages:
            role = msg.get('role')
            content = msg.get('content')
            if role == 'system':
                if isinstance(content, str):
                    system_parts.append(content)
                continue
            blocks = []
            if isinstance(content, str):
                blocks.append({'type': 'text', 'text': content})
            elif isinstance(content, list):
                for block in content:
                    if block.get('type') == 'text':
                        blocks.append({'type': 'text', 'text': block.get('text', '')})
                    elif block.get('type') == 'image_url':
                        url = (block.get('image_url') or {}).get('url', '')
                        match = re.match(r'data:([^;]+);base64,(.*)$', url, re.S)
                        if match:
                            blocks.append({
                                'type': 'image',
                                'source': {
                                    'type': 'base64',
                                    'media_type': match.group(1),
                                    'data': match.group(2),
                                },
                            })
            if not blocks:
                continue
            out.append({
                'role': role if role in ('user', 'assistant') else 'user',
                'content': blocks,
            })
        return system_parts, out

    def get_claude(self, data, author_id, answer_id, param={}):
        self.ensure_one()
        if not self.openapi_api_key or not self.endpoint:
            raise UserError(_("Please provide Ai Robot [%s] API Key and Endpoint URL first." % self.name))

        if isinstance(data, list):
            messages = data
        else:
            messages = [{"role": "user", "content": data}]

        # 处理传参，传过来的优先于 robot 默认的
        max_tokens = param.get('max_tokens') or self.max_tokens or 1024
        temperature = param.get('temperature') if param.get('temperature') else self.temperature
        top_p = param.get('top_p') if param.get('top_p') else self.top_p

        system_parts, claude_messages = self._claude_convert_messages(messages)
        # Ai角色设定，如果没设定则再处理
        sys_content = self.get_ai_system(param.get('sys_content'))
        if sys_content:
            system_parts.insert(0, sys_content['content'])

        pdata = {
            'model': self.ai_model,
            'messages': claude_messages,
            'max_tokens': max_tokens,
        }
        if system_parts:
            pdata['system'] = '\n'.join(system_parts)
        if temperature:
            pdata['temperature'] = temperature
        if top_p:
            pdata['top_p'] = top_p

        R_TIMEOUT = self.ai_timeout or 120
        try:
            response = requests.post(self.endpoint, headers=self._claude_headers(), json=pdata, timeout=R_TIMEOUT)
            response.close()
        except Exception as e:
            _logger.warning('=====================claude request error: %s' % e)
            return _("Response Timeout, please speak again.")
        if not response:
            return _("Response Timeout, please speak again.")

        res = response.json()
        if res.get('type') == 'error':
            _logger.warning('=====================claude output data: %s' % res)
            return res.get('error', {}).get('message') or _("Response Timeout, please speak again.")

        # 转成 openai 风格，统一走 get_ai_post 后置处理与上下文
        content_text = ''.join(
            block.get('text', '') for block in res.get('content', []) if block.get('type') == 'text'
        )
        usage = res.get('usage', {})
        return {
            'usage': {
                'prompt_tokens': usage.get('input_tokens', 0),
                'completion_tokens': usage.get('output_tokens', 0),
                'total_tokens': usage.get('input_tokens', 0) + usage.get('output_tokens', 0),
            },
            'choices': [{'message': {'role': 'assistant', 'content': content_text}}],
        }

    def get_ai_post(self, res, author_id=False, answer_id=False, param={}):
        if self.provider == 'claude':
            if not res or not isinstance(res, dict) or 'choices' not in res:
                return res, False, False
            usage = res['usage']
            content = res['choices'][0]['message']['content']
            return content, usage, True
        else:
            return super().get_ai_post(res, author_id, answer_id, param)

    def get_ai_list_model(self):
        self.ensure_one()
        if self.provider == 'claude':
            if not self.openapi_api_key:
                raise UserError(_("Please provide Ai Robot [%s] API Key." % self.name))
            headers = self._claude_headers()
            R_TIMEOUT = self.ai_timeout or 120
            o_url = CLAUDE_MODELS_URL
            response = requests.get(o_url, headers=headers, timeout=R_TIMEOUT)
            response.close()
            if response:
                res = response.json()
                r_text = json.dumps(res, indent=2)
            else:
                r_text = 'No response.'
            raise UserError(r_text)
        else:
            return super().get_ai_list_model()
