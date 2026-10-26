# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

import requests

from odoo import api, fields, models, release, _

_logger = logging.getLogger(__name__)


class ErrorSubmitWizard(models.TransientModel):
    _name = 'error.submit.wizard'
    _description = 'Error Submit Wizard'

    issue_url = fields.Char(string='Issue URL', default='http://localhost', help='Issue URL where the error occurred')
    issue_title = fields.Char(string='Issue Title')

    # v13 表单单点击会先保存记录再执行动作，出错时 traceback 可能为空，
    # 故此处不做 required 校验（v18 由 JS 拦截提交，不受此限制）
    issue_body = fields.Text(
        string='Issue Body',
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
        default='https://www.odooai.cn/service/error-report',
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
        dbuuid = self.env['ir.config_parameter'].sudo().get_param('database.uuid', '')
        defaults['dbuuid'] = dbuuid

        defaults['submit_login'] = self.env.user.login

        if 'error_report_url' in fields_list:
            error_report_url = self.env['ir.config_parameter'].sudo().get_param(
                'app_saas.error_report_url',
                'https://www.odooai.cn/service/error-report'
            )
            defaults['error_report_url'] = error_report_url

        return defaults

    def action_submit_error(self):
        """向后端服务提交报错信息（v13 由服务端请求，避免浏览器 CORS 限制）"""
        self.ensure_one()
        url = self.error_report_url or 'https://www.odooai.cn/service/error-report'
        payload = {
            'issue_url': self.issue_url or 'http://localhost',
            'issue_title': self.issue_title or _('Odoo Error Report'),
            'issue_body': self.issue_body or '',
            'dbuuid': self.dbuuid or '',
            'submit_login': self.submit_login or '',
            'submit_type': self.submit_type or 'public',
            'odoo_version': self.odoo_version or release.version,
            'timestamp': fields.Datetime.to_string(fields.Datetime.now()),
            'user_name': self.env.user.name or '',
            'user_email': self.env.user.email or '',
        }

        try:
            response = requests.post(
                url, json=payload, timeout=30,
                headers={'User-Agent': 'OdooAppSaas-Client/13.0'},
            )
        except Exception as e:
            _logger.warning('app_saas error submit failed: %s', e)
            return self._notify_result(False, _('Cannot connect to the server, please check the network (%s)') % e)

        try:
            result = response.json() if response.text else {}
        except ValueError:
            result = {}
        _logger.info('app_saas error submit response: %s %s', response.status_code, result)

        if response.ok and result.get('success'):
            ticket_id = result.get('ticket_id') or 'N/A'
            return self._notify_result(
                True, _('Error report submitted to odooai.cn, ticket %s.') % ticket_id, ticket_id)
        message = result.get('message') or 'HTTP %s: %s' % (response.status_code, response.reason)
        return self._notify_result(False, message)

    def _notify_result(self, success, message, ticket_id=None):
        """返回 v13 display_notification 动作，前端 JS 拦截后可额外关闭向导"""
        return {
            'success': success,
            'message': message,
            'ticket_id': ticket_id,
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Submitted') if success else _('Submit Failed'),
                'message': message,
                'type': 'success' if success else 'danger',
                'sticky': not success,
            },
        }
