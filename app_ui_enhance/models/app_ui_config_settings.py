# -*- coding: utf-8 -*-

# Created on 2017-11-16
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

import logging

from openerp import api, fields, models, _

_logger = logging.getLogger(__name__)


class AppUiConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'app.ui.config.settings'

    _description = u"App Web UI enhance settings"
    app_ui_show_search_date = fields.Boolean('Show date range search in tree/pivot view', help=u"Set 'True' to show, Set 'False' to hide")
    app_ui_show_search_number = fields.Boolean('Show number range search tree/pivot view', help=u"Set 'True' to show, Set 'False' to hide")

    @api.model
    def get_default_all(self, fields):
        ir_config = self.env['ir.config_parameter']
        app_ui_show_search_date = True if ir_config.get_param('app_ui_show_search_date') == "True" else False
        app_ui_show_search_number = True if ir_config.get_param('app_ui_show_search_number') == "True" else False

        return dict(
            app_ui_show_search_date=app_ui_show_search_date,
            app_ui_show_search_number=app_ui_show_search_number
        )

    @api.multi
    def set_default_all(self):
        self.ensure_one()
        ir_config = self.env['ir.config_parameter']
        ir_config.set_param("app_ui_show_search_date", self.app_ui_show_search_date or "False")
        ir_config.set_param("app_ui_show_search_number", self.app_ui_show_search_number or "False")
        return True
