# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_doc_root_url = fields.Char('Help of topic domain', config_parameter='app_doc_root_url', default='https://www.odooai.cn')

    def action_set_app_doc_root_to_my(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        self.env['ir.config_parameter'].sudo().set_param('app_doc_root_url', base_url)

    def action_set_app_doc_root_to_odooai(self):
        base_url = 'https://www.odooai.cn'
        self.env['ir.config_parameter'].sudo().set_param('app_doc_root_url', base_url)
