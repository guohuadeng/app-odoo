# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Base(models.AbstractModel):
    _inherit = 'base'

    # name_en_US 只要某个模型有此字段，且放在界面上，就会进行此处理
    # 无此字段不处理

    # todo: 为了性能，暂时不在 create 时处理
    # todo: create_multi ?
    # todo: 在 ir.translation 中处理以提高性能， 或反向写回
    @api.model
    def create(self, vals):
        name_field = self._fields.get("name")
        name_en_field = self._fields.get("name_en_US")
        name_en_US = None
        if name_field and name_field.translate and name_field.type in ["char", "text"] \
                and name_en_field and name_en_field.type in["char", "text"] and 'name_en_US' in vals:
            name_en_US = vals.get('name_en_US')
        rec = super(Base, self).create(vals)
        if name_en_US:
            try:
                rec.with_context(lang='en_US').name = name_en_US
            except Exception as e:
                pass
        return rec

    def write(self, vals):
        name_field = self._fields.get("name")
        name_en_field = self._fields.get("name_en_US")
        if name_field and name_field.translate and name_field.type in ["char", "text"] \
                and name_en_field and name_en_field.type in["char", "text"] and 'name_en_US' in vals:
            name_en_US = vals.get('name_en_US')
            if name_en_US != None:
                try:
                    self.with_context(lang='en_US').write(dict(name=name_en_US))
                except Exception as e:
                    pass
        return super(Base, self).write(vals)
