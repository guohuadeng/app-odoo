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

    # todo: 以下处理方式不同，最好直接做一个widget，
    #  非开发者模式时，能显示出非英文时值，并可点击改多语种。
    # 将原 widget加 options 处理
    @api.model_create_multi
    def create(self, vals_list):
        res = super(MixinNameEn, self).create(vals_list)
        if self.env.lang == 'en_US':
            return res

        # todo: 这里已为了提高性能不检查。不需检查当前odoo是否有英文，没英文就不给安装此模块。同时也不检查条件
        # if name_field and name_field.translate and name_field.type in ["char", "text"]:
        #     # todo: 符合条件，后续为提高性能，无需做此判断
        #     pass
        # else:
        #     return res
        # 处理写 en
        for index, vals in enumerate(vals_list):
            name_en_US = vals.get('name_en_US')
            if name_en_US:
                try:
                    res[index].with_context(lang='en_US').write(dict(name=name_en_US))
                except Exception as e:
                    _logger.error('============== name_en mixin create error from name_en_US: %s' % str(e))
        return res

    def write(self, vals):
        res = super(MixinNameEn, self).write(vals)
        if self.env.lang == 'en_US':
            return res

        name_en_US = vals.get('name_en_US')
        name = vals.get('name')
        if name_en_US:
            try:
                self.with_context(lang='en_US').write(dict(name=name_en_US))
            except Exception as e:
                _logger.error('============== name_en mixin write error:%s' % str(e))
        return res
