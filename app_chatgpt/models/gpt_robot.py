# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class GptRobot(models.Model):
    _name = 'gpt.robot'
    _description = 'Gpt Robot'

    name = fields.Char(string='Name')
    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here")
    temperature = fields.Float(string='Temperature')
