# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_context_timeout = fields.Integer(string="Connect Timout", help="群聊中多少分钟以内的聊天信息作为上下文继续", config_parameter="app_chatgpt.openapi_context_timeout")
    openai_sync_config = fields.Selection([
        ('sync', 'Synchronous'),
        ('async', 'Asynchronous')
    ], string='Sync Config', default='sync', config_parameter="app_chatgpt.openai_sync_config")
    module_app_ai_bard = fields.Boolean("Google Bard Ai")
    module_app_ai_baidu = fields.Boolean("Baidu Ai China", help='百度文心一格')
    module_app_ai_ali = fields.Boolean("Ali Ai China", help='阿里通义千问')
