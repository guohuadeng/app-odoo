# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    short_name = fields.Char('Short Name')  # 简称

    # ref，编码限制在 app_partner_auto_reference
    # 显示[编码]简称
    @api.multi
    def name_get(self):
        result = []
        name = ''
        for partner in self:
            if partner.ref:
                try:
                    name = '[' + partner.ref + ']'
                except:
                    name = ''
            if partner.short_name:
                name = name + partner.short_name
            elif partner.name:
                name = name + partner.name
            else:
                name = name
            result.append((partner.id, name))
        return result


class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    _order = 'sequence, name'

    sequence = fields.Integer('Sequence', help="Used to order partner category")
