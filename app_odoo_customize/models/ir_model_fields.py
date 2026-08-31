# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, SUPERUSER_ID, tools,  _

_logger = logging.getLogger(__name__)


class IrModelFields(models.Model):
    _inherit = 'ir.model.fields'

    # 调整显示 field name：o19 已移除 name_get()，显示定制迁移至 _compute_display_name（显示格式保持原 name_get 行为）
    @api.depends('field_description', 'model')
    def _compute_display_name(self):
        for field in self:
            if self.env.context.get('hide_model'):
                # 保持 o19 原生 hide_model 行为
                field.display_name = field.field_description
            elif self.env.context.get('show_field_description_only', False):
                field.display_name = field.field_description
            else:
                field.display_name = '%s (%s,%s)' % (field.field_description, field.name, field.model)

    # 调整可按 field name查询；o19 name_search 参数改名 args→domain
    @api.model
    def name_search(self, name='', domain=None, operator='ilike', limit=None, order=None):
        """
        name search that supports searching by tag code
        """
        if name:
            full_domain = ['|', ('name', operator, name), ('field_description', operator, name)]
            res = self.search_fetch(full_domain, ['display_name'], limit=limit)
            return [(rec.id, rec.display_name) for rec in res]
        return super().name_search(name, domain, operator, limit, order)
