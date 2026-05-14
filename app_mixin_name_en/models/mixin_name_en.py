# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MixinNameEn(models.AbstractModel):
    _name = 'mixin.name.en'
    _description = 'Mixin Auto english name'

    name_en_US = fields.Char('English Name', inverse='_inverse_name_en_US')

    def _inverse_name_en_US(self):
        for rec in self:
            name_field = rec._fields.get('name')
            if name_field and name_field.translate:
                rec.with_context(lang='en_US').write({'name': rec.name_en_US})

