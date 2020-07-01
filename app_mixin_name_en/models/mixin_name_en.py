# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class MixinNameEn(models.AbstractModel):
    _name = 'mixin.name.en'
    _description = 'Mixin Auto english name'

    # name_en_US 只要某个模型有此字段，且放在界面上，就会进行此处理
    # 无此字段不处理

    name_en_US = fields.Char('English Name')

    # create_multi 中不可用，因为须先 create 再写 lang=en_US的值
    # todo: 在 ir.translation 中处理以提高性能， 或反向写回

    @api.model
    def create(self, vals):
        name_field = self._fields.get("name")
        name_en_US = None

        if name_field and name_field.translate and name_field.type in ["char", "text"] and 'name_en_US' in vals and vals.get('name_en_US'):
            name_en_US = vals.get('name_en_US')
        rec = super(MixinNameEn, self).create(vals)
        if name_en_US and self.env.lang != 'en_US':
            try:
                rec.with_context(lang='en_US').write(dict(name=name_en_US))
            except Exception as e:
                pass
        return rec

    def write(self, vals):
        name_field = self._fields.get("name")
        name_en_US = None
        if name_field and name_field.translate and name_field.type in ["char", "text"] and 'name_en_US' in vals and vals.get('name_en_US'):
            name_en_US = vals.get('name_en_US')
        rec = super(MixinNameEn, self).write(vals)
        if name_en_US and self.env.lang != 'en_US':
            try:
                self.with_context(lang='en_US').write(dict(name=name_en_US))
            except Exception as e:
                pass
        return rec
