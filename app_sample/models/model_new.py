# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.

#    Create on 2023-10-06
##############################################################################

from odoo import models, fields, api, _
from odoo.tools.translate import html_translate

from datetime import datetime, timedelta
import logging
_logger = logging.getLogger(__name__)


# Template for model New
class ModelNew(models.Model):
    
    _name = 'model.new'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Model New'
    _order = 'sequence,name'
    
    # Base field
    name = fields.Char(string='Name', translate=True, required=True, readonly=False, copy=True)
    ref = fields.Char(string='Reference', required=True, readonly=False, copy=False, index=True)
    image = fields.Binary(string="Image")
    amount = fields.Float(string="Amount", digits="Product Price")
    note = fields.Text(string='Note', readonly=False, copy=True)
    website_description = fields.Html(
        'Description for the website', translate=html_translate,
        sanitize_overridable=True,
        sanitize_attributes=False, sanitize_form=False)
    date = fields.Datetime(string="Date", default=lambda self: fields.Datetime.now())
    
    # Relation field
    partner_ids = fields.Many2many(comodel_name="res.partner",
                                   relation="model_new_res_partner_rel",
                                   column1="new_id", column2="partner_id",
                                   string="many2many_tags_avatar")
    
    partner_count = fields.Integer(string="#Partner", compute='_compute_partner_count', store=True)
    
    # product_ids = fields.One2many(comodel_name="product.product",
    #                               inverse_name="model_new_id",
    #                               string="Model New")
    
    user_id = fields.Many2one('res.users', string='many2one_avatar_user',
                              required=False, index=True, default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string='Company',
                                 required=False, index=True, default=lambda self: self.env.company)
    
    # Extra field
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer('Sequence', default=99, help="Determine the display order")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string="State", selection=[
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', "Cancelled"),
    ], default='draft', required=False)
    
    # begin widget
    # char, text, html
    w_phone = fields.Char(string='phone', default='13925100000')
    w_email = fields.Char(string='email', default='info@example.com')
    w_image_url = fields.Char(string='image_url', default='https://www.odooai.cn/web/image/website/1/logo')
    w_url = fields.Char(string='url', default='https://www.odooai.cn')
    w_CopyClipboardURL = fields.Char(string='CopyClipboardURL', default='https://www.odooai.cn')
    w_CopyClipboardChar = fields.Char(string='CopyClipboardChar', default='https://www.odooai.cn')
    w_CopyClipboardText = fields.Char(string='CopyClipboardText', default='https://www.odooai.cn')
    
    # int
    date_end = fields.Datetime(string="Date End", default=lambda self: fields.Datetime.now() + timedelta(days=30))
    day_max = fields.Integer(string="Left Days Max", default=100)
    w_gauge = fields.Integer(
        'gauge', compute='_compute_gauge',
        help='Left date to date end，剩下的天数')
    w_progressbar = fields.Float(string='progressbar')
    
    # float
    w_percentpie = fields.Float(string='percentpie', related='w_progressbar')
    w_percentage = fields.Float(string='percentage')
    
    # selection
    w_status_with_color = fields.Selection(string="status_with_color", selection=[
        ('color1', 'Color1'),
        ('color2', 'Color2'),
        ('color3', "Color3"),
    ], default='color1', required=False)
    w_color_s = fields.Integer(string='status_with_color Color Index')
    
    # m2o
    w_selection_badge = fields.Many2one('res.partner', string='selection_badge')
    
    # m2m
    w_autosave_many2many_tags = fields.Many2many(comodel_name="res.partner",
                                   relation="model_new_res_partner_rel_w_autosave_many2many_tags",
                                   column1="new_id", column2="partner_id",
                                   string="autosave_many2many_tags")
    
    w_date_begin = fields.Char(string='Date Begin')
    w_date_end = fields.Char(string='Date End')
    w_toggle_button = fields.Boolean(string='toggle_button')
    w_res_partner_many2one = fields.Char(string='Boolean toggle')
    
    _sql_constraints = [('uniq_ref', 'unique(ref)', 'The reference must be unique.')]
    
    @api.depends('date', 'date_end')
    def _compute_gauge(self):
        for rec in self:
            rec.w_gauge = (rec.date_end - rec.date).days

    @api.depends('partner_ids')
    def _compute_partner_count(self):
        for rec in self:
            rec.partner_count = len(rec.partner_ids)



