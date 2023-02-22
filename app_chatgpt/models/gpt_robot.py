# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class GptRobot(models.Model):
    _name = 'gpt.robot'
    _description = 'Gpt Robot'
    _order = 'sequence, name'

    name = fields.Char(string='Name')
    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here")
    temperature = fields.Float(string='Temperature', default=0.9)
    sequence = fields.Integer('Sequence', help="Determine the display order", default=10)
