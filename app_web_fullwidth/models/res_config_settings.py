# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # todo: 可能要设置为不同公司不同
    default_chatter_position = fields.Selection([
        ("auto", "Responsive"),
        ("bottom", "Bottom"),
        ("sided", "Sided"),
        ], string='Default Chatter Position', default="bottom", default_model="res.users")

    def user_set_chatter_pos(self):
        # todo: 处理设置
        company_id = self.env.company.id
        users = self.env['res.users'].with_context(active_test=False).search([('company_id', '=', company_id)])
        if users:
            users.write({
                'chatter_position': self.default_chatter_position
            })
        pass
