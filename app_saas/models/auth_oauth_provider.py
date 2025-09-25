# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, tools, _

import base64
from datetime import timedelta

class AuthOAuthProvider(models.Model):

    _inherit = 'auth.oauth.provider'
    _order = 'sequence, name'

    # 取code的url，主要针对国内的先取code，再拿Token的方式
    code_endpoint = fields.Char(string='Token by Code Endpoint', help='Get Token from Code. Only for Code response type.')
    user_template_id = fields.Many2one('res.users', string='New User Template',
                                       domain=[('active', '=', False)])
