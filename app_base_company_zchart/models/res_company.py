# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"

    _parent_store = True
    parent_path = fields.Char(index=True, unaccent=False)
    
    # 注意，res.partner 有 parent_id 和 child_ids
    all_child_ids = fields.One2many('res.company', string='All Child Companies', compute='_compute_all_child_ids')
    
    @api.depends('parent_id', 'child_ids')
    def _compute_all_child_ids(self):
        pass
        
