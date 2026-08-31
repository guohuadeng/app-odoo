# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import requests

from odoo import api, fields, models, release, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ErrorSubmitWizard(models.TransientModel):
    _name = 'error.submit.wizard'
    _description = 'Error Submit Wizard'

    issue_url = fields.Char(string='Issue URL', default='http://localhost', help='Issue URL where the error occurred')
    issue_title = fields.Char(string='Issue Title')

    issue_body = fields.Text(
        string='Issue Body',
        required=True,
        help='Issue Body, typically traceback traceback information'
    )
    odoo_version = fields.Char(string='Odoo Version')
    dbuuid = fields.Char(
        string='Database UUID',
        readonly=True,
        help='Database UUID of the current instance of Odoo'
    )

    submit_login = fields.Char(
        string='Submit Login',
        readonly=True,
        help='Login ID of the user submitting the error report'
    )

    error_report_url = fields.Char(
        string='Error Report URL',
        default='https://www.odooapp.cn/api/v1/error-report',
        help='URL to submit the error report to'
    )

    submit_type = fields.Selection(
        selection=[
            ('public', 'Public'),
            ('ticket', 'Ticket'),
        ], string='Submit Type', default='public', required=True,
        help='Select how to submit the error report: Ticket (private) or Public (forum).'
    )

    @api.model
    def default_get(self, fields_list):
        defaults = super(ErrorSubmitWizard, self).default_get(fields_list)

        ctx = self.env.context or {}

        if 'issue_url' in fields_list:
            defaults['issue_url'] = ctx.get('default_issue_url', 'http://localhost')

        # 设置issue_body (traceback)
        if 'issue_body' in fields_list:
            error_data = ctx.get('default_issue_body', {})
            defaults['issue_body'] = error_data

        if 'issue_title' in fields_list:
            defaults['issue_title'] = ctx.get('default_issue_title', 'Odoo错误报告')

        defaults['odoo_version'] = release.version
        # if 'dbuuid' in fields_list:
        dbuuid = self.env['ir.config_parameter'].sudo().get_param('database.uuid', '')
        defaults['dbuuid'] = dbuuid

        # if 'submit_login' in fields_list:
        defaults['submit_login'] = self.env.user.login

        if 'error_report_url' in fields_list:
            error_report_url = self.env['ir.config_parameter'].sudo().get_param(
                'app_saas.error_report_url',
                'https://www.odooapp.cn/api/v1/error-report'
            )
            defaults['error_report_url'] = error_report_url

        return defaults

    def action_submit_error(self):
        """
        此方法已由前端JS接管处理
        """
        pass
