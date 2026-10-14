# -*- coding: utf-8 -*-

from odoo import api, fields, models


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    def write(self, vals):
        # 处理强制全局, Create时不管
        for view in self:
            if len(view.page_ids) == 1:
                page = view.page_ids[0]
                if page.is_force_all:
                    self = self.with_context(no_cow=1)
        return super(IrUiView, self).write(vals)
