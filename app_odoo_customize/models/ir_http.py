# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import models, api, _
from odoo.http import request

_logger = logging.getLogger(__name__)

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        try:
            config_parameter = request.env['ir.config_parameter'].sudo()
        except Exception as e:
            config_parameter = self.env['ir.config_parameter'].sudo()
            _logger.warning("Error while getting config parameter: %s", e)
            
        result['app_system_name'] = config_parameter.get_param('app_system_name', 'odooAi')
        result['app_documentation_url'] = config_parameter.get_param('app_documentation_url', 'https://www.odooai.cn/r/yh18')
        result['app_documentation_dev_url'] = config_parameter.get_param('app_documentation_dev_url', 'https://www.odooai.cn/r/kf18')
        result['app_support_url'] = config_parameter.get_param('app_support_url', 'https://www.odooai.cn/trial')
        result['app_account_title'] = config_parameter.get_param('app_account_title', _('我的Ai服务中心'))
        result['app_account_url'] = config_parameter.get_param('app_account_url', 'https://www.odooai.cn/my')
        result['app_show_lang'] = config_parameter.get_param('app_show_lang', True)
        result['app_show_debug'] = config_parameter.get_param('app_show_debug', False)
        result['app_show_documentation'] = config_parameter.get_param('app_show_documentation', True)
        result['app_show_documentation_dev'] = config_parameter.get_param('app_show_documentation_dev', True)
        result['app_show_support'] = config_parameter.get_param('app_show_support', True)
        result['app_show_account'] = config_parameter.get_param('app_show_account', True)
        result['app_show_poweredby'] = config_parameter.get_param('app_show_poweredby', False)
        # 增加多语言
        result['app_lang_list'] = self.env['res.lang'].search_read([], ['id', 'code', 'name', 'flag_image_url'])
        result['is_erp_manager'] = self.env.user.has_group('base.group_erp_manager')
        # 增加 bar位置处理
        result['app_navbar_pos_pc'] = config_parameter.get_param('app_navbar_pos_pc', 'top')
        result['app_navbar_pos_mobile'] = config_parameter.get_param('app_navbar_pos_mobile', 'top')
        # 此处直接取，不用 session
        result['app_debug_only_admin'] = config_parameter.get_param('app_debug_only_admin', True)
        result['app_stop_subscribe'] = config_parameter.get_param('app_stop_subscribe', False)
        result['app_doc_root_url'] = config_parameter.get_param('app_doc_root_url', 'https://www.odooai.cn')
        return result
