# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(translate=False)
    short_name = fields.Char('Short Name')  # 简称
    fax = fields.Char('Fax')  # 简称

    # 增加地址显示中的手机号与电话号码
    # 选项 show_address 开启则增加显示手机与电话号
    def _get_name(self):
        name = super(ResPartner, self)._get_name()
        partner = self
        if self._context.get('show_address'):
            if partner.mobile and partner.phone:
                name = name + "\n" + partner.mobile + "," + partner.phone
            elif partner.mobile:
                name = name + "\n" + partner.mobile
            elif partner.phone:
                name = name + "\n" + partner.phone
        return name.strip()

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if 'lang' not in values:
                values['lang'] = 'zh_CN'
        return super(ResPartner, self).create(vals_list)
