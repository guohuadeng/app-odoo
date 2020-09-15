# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    short_name = fields.Char('Short Name', related='partner_id.short_name', readonly=False)

    # 当传参 show_short_company 时，只显示简称
    def name_get(self):
        if self._context.get('show_short_company'):
            return [(value.id, "%s" % (value.short_name if value.short_name else value.name)) for value in self]
        else:
            return super().name_get()
