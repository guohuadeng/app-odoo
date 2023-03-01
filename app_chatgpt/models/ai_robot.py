# -*- coding: utf-8 -*-

import requests
from odoo import api, fields, models, _


class AiRobot(models.Model):
    _name = 'ai.robot'
    _description = 'Gpt Robot'
    _order = 'sequence, name'

    name = fields.Char(string='Name')
    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here")
    temperature = fields.Float(string='Temperature', default=0.9)
    sequence = fields.Integer('Sequence', help="Determine the display order", default=10)

    def action_disconnect(self):
        requests.delete('https://chatgpt.com/v1/disconnect')

