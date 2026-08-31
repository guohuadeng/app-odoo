# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    chatter_position = fields.Selection([
        ("auto", "Responsive"),
        ("bottom", "Bottom"),
        ("sided", "Sided"),
        ], string='Chatter Position', default="bottom")

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ["chatter_position"]

    @property
    def SELF_WRITEABLE_FIELDS(self):
        return super().SELF_WRITEABLE_FIELDS + ["chatter_position"]

    # ----------------------------------------------------------
    # 缓存失效与页面重载
    # ----------------------------------------------------------

    @api.model
    def _get_invalidation_fields(self):
        """扩展失效字段集合，使 chatter_position 变更后清除缓存。
            与 Odoo 原生 'lang' 字段使用相同模式。
        """
        return super()._get_invalidation_fields() | {'chatter_position'}
