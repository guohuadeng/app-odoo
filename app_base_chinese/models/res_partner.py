# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # name = fields.Char(translate=False)
    short_name = fields.Char('Short Name')  # 简称
    fax = fields.Char('Fax')  # 简称

    # 增加地址显示中的手机号与电话号码
    # 选项 show_address 开启则增加显示手机与电话号（o19 已删 _get_name/mobile 字段，迁移至 _compute_display_name 仅用 phone）
    @api.depends('complete_name', 'email', 'vat', 'state_id', 'country_id', 'commercial_company_name',
                 'phone')
    @api.depends_context(
        'show_address', 'partner_show_db_id',
        'show_email', 'show_vat', 'lang', 'formatted_display_name'
    )
    def _compute_display_name(self):
        super(ResPartner, self)._compute_display_name()
        if self._context.get('show_address'):
            for partner in self:
                name = partner.display_name
                if partner.phone:
                    name = name + "\n" + partner.phone
                partner.display_name = name.strip()

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if 'lang' not in values:
                values['lang'] = 'zh_CN'
        return super(ResPartner, self).create(vals_list)
