# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError

class Report(models.Model):
    _inherit = 'report'

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

    def barcode(self, barcode_type, value, width=600, height=100, humanreadable=0):
        ir_config = self.env['ir.config_parameter']
        app_ui_force_barcode = ir_config.get_param('app_ui_force_barcode', default='Default')
        if app_ui_force_barcode or app_ui_force_barcode == 'Default':
            return super(Report, self).barcode(barcode_type, value, width, height, humanreadable)
        else:
            return super(Report, self).barcode(app_ui_force_barcode, value, width, height, humanreadable)
