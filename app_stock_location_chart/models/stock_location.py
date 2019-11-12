# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Location(models.Model):
    _name = "stock.location"
    _inherit = ['stock.location', 'image.mixin']

    child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_child_all_count', store=False)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)
