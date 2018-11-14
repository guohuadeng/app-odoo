# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    short_name = fields.Char('Short Name')  # 简称

    # 在原唯一检查中增加ref唯一
    _sql_constraints = [
        ('uniq_ref', 'unique(ref)', _('The reference must be unique')),
    ]

    @api.constrains('ref')
    def _check_ref(self):
        customers = self.search([('ref', '=', self.ref)], limit=2)
        if len(customers) > 1:
            raise ValidationError(_('The reference must be unique!'))

    # 显示[编码]简称
    @api.multi
    def name_get(self):
        result = []
        for partner in self:
            if partner.short_name:
                name = partner.short_name
            else:
                name = partner.name
            if partner.ref:
                name = '[' + partner.ref + ']' + name
            result.append((partner.id, name))
        return result


class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    _order = 'sequence, parent_left, name'

    sequence = fields.Integer('Sequence', help="Used to order partner category")


