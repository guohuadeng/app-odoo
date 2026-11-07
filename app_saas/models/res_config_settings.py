# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_app_cn_po = fields.Boolean('SaaS Chinese PO', help="Checked to Sync Odoo Chinese from www.odooapp.cn")
    app_saas_db_token = fields.Char('Cloud DB Token', default=None, config_parameter='app_saas_db_token',
                                    help="The odooapp SaaS Token for this Odoo Database. You can reset in https://www.odooapp.cn")

    # ------------------------------------------------------------------
    # 通用云通道（Cloud Tunnel）：总开关与连接地址由管理员在这里配置；
    # 运行时状态由 app_saas_tunnel 的 agent 上报写入 ir.config_parameter，
    # 本模块只做展示，不 import app_saas_tunnel，避免反向依赖。
    # ------------------------------------------------------------------

    is_cloud_tunnel_enabled = fields.Boolean(
        string='Enable Cloud Tunnel',
        config_parameter='app_saas.is_cloud_tunnel_enabled',
        default=True,
        help='Enable the outbound cloud tunnel. When off, the tunnel agent disconnects and the bridge refuses new keys.',
    )
    cloud_tunnel_url = fields.Char(
        string='Cloud Tunnel URL',
        config_parameter='app_saas.cloud_tunnel_url',
        default='https://www.odooapp.cn',
        help='Base URL of the cloud hub, e.g. https://www.odooapp.cn',
    )
    cloud_tunnel_key = fields.Char(
        string='Cloud Tunnel Key',
        compute='_compute_cloud_tunnel_key',
        help='Routing key of this instance on the cloud hub. Defaults to the database UUID and matches oauth2.client.client_id on the cloud side.',
    )
    cloud_tunnel_status = fields.Selection(
        selection=[
            ('disabled', 'Disabled'),
            ('connecting', 'Connecting'),
            ('online', 'Online'),
            ('offline', 'Offline'),
            ('error', 'Error'),
        ],
        string='Cloud Tunnel Status',
        compute='_compute_cloud_tunnel_state',
    )
    cloud_tunnel_last_seen = fields.Datetime(
        string='Last Seen',
        compute='_compute_cloud_tunnel_state',
        help='Last heartbeat received from the tunnel agent.',
    )
    cloud_tunnel_last_error = fields.Text(
        string='Last Error',
        compute='_compute_cloud_tunnel_state',
        help='Most recent error reported by the tunnel agent.',
    )

    @api.depends('is_cloud_tunnel_enabled')
    def _compute_cloud_tunnel_key(self):
        """路由键：优先取显式配置，缺省回退 database.uuid（与云端 client_id 一致）。"""
        icp = self.env['ir.config_parameter'].sudo()
        key = icp.get_str('app_saas.cloud_tunnel_key')
        for rec in self:
            rec.cloud_tunnel_key = key or icp.get_str('database.uuid')

    def _compute_cloud_tunnel_state(self):
        """运行状态只读展示，值由 app_saas_tunnel 写入参数。"""
        icp = self.env['ir.config_parameter'].sudo()
        status = icp.get_str('app_saas.cloud_tunnel_status')
        last_seen = icp.get_str('app_saas.cloud_tunnel_last_seen')
        last_error = icp.get_str('app_saas.cloud_tunnel_last_error')
        for rec in self:
            rec.cloud_tunnel_status = status or (
                'disabled' if not rec.is_cloud_tunnel_enabled else 'offline')
            rec.cloud_tunnel_last_seen = last_seen or False
            rec.cloud_tunnel_last_error = last_error or False
