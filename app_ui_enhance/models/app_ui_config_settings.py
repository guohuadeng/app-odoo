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

    """Contoller able to render barcode images thanks to reportlab.
    Samples:
        <img t-att-src="'/report/barcode/QR/%s' % o.name"/>
        <img t-att-src="'/report/barcode/?type=%s&amp;value=%s&amp;width=%s&amp;height=%s' %
            ('QR', o.name, 200, 200)"/>

    :param type: Accepted types: 'Codabar', 'Code11', 'Code128', 'EAN13', 'EAN8', 'Extended39',
    'Extended93', 'FIM', 'I2of5', 'MSI', 'POSTNET', 'QR', 'Standard39', 'Standard93',
    'UPCA', 'USPS_4State'
    :param humanreadable: Accepted values: 0 (default) or 1. 1 will insert the readable value
    at the bottom of the output image
    """
    
    app_ui_force_barcode = fields.Selection([
        ('Default', 'Odoo Default'),
        ('Code128', 'Code128'),
        ('Standard39', 'Standard39'),
        ('EAN13', 'EAN13'),
        ('QR', 'QR'),
        ('Codabar', 'Codabar'),
        ('Code11', 'Code11'),
        ('Extended39', 'Extended39'),
        ('EAN8', 'EAN8'),
        ('Extended93', 'Extended93'),
        ('FIM', 'FIM'),
        ('I2of5', 'I2of5'),
        ('MSI', 'MSI'),
        ('POSTNET', 'POSTNET'),
        ('Standard93', 'Standard93'),
        ('UPCA', 'UPCA'),
        ('USPS_4State', 'USPS_4State'),
    ], string='Force all Odoo Barcode to:', help=u"Set Odoo Default to use the barcode odoo define in report(EAN13).")

    app_ui_allow_barcode = fields.Char('Allow Barcode, Seperated by ","', help=u"Default Allow QR and Standard39.")

    @api.model
    def get_default_all(self, fields):
        ir_config = self.env['ir.config_parameter']
        app_ui_show_search_date = True if ir_config.get_param('app_ui_show_search_date') == "True" else False
        app_ui_show_search_number = True if ir_config.get_param('app_ui_show_search_number') == "True" else False
        app_ui_force_barcode = ir_config.get_param('app_ui_force_barcode')
        app_ui_allow_barcode = ir_config.get_param('app_ui_allow_barcode')

        return dict(
            app_ui_show_search_date=app_ui_show_search_date,
            app_ui_show_search_number=app_ui_show_search_number,
            app_ui_force_barcode=app_ui_force_barcode,
            app_ui_allow_barcode=app_ui_allow_barcode
        )

    @api.multi
    def set_default_all(self):
        self.ensure_one()
        ir_config = self.env['ir.config_parameter']
        ir_config.set_param("app_ui_show_search_date", self.app_ui_show_search_date or "False")
        ir_config.set_param("app_ui_show_search_number", self.app_ui_show_search_number or "False")
        ir_config.set_param("app_ui_force_barcode", self.app_ui_force_barcode or "Default")
        ir_config.set_param("app_ui_allow_barcode", self.app_ui_allow_barcode or "")
        return True
