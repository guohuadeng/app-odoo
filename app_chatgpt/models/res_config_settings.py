# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_context_timeout = fields.Integer(string="上下文连接超时", help="多少秒以内的聊天信息作为上下文继续", config_parameter="app_chatgpt.openapi_context_timeout")
