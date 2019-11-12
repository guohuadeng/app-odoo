# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"

    # 注意，res.partner 有 parent_id 和 child_ids
    _parent_name = "parent_id"

