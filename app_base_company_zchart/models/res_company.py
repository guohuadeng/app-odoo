# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"

    _parent_store = True
    parent_path = fields.Char(index=True)

    # 注意，res.partner 有 parent_id 和 child_ids
    # all_child_ids = fields.One2many('res.company', string='All Child Companies', compute=False)
    #
    # @api.depends('parent_id', 'child_ids')
    # def _compute_all_child_ids(self):
    #     pass
    #

    def force_write_parent_id(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_base_company_zchart.action_force_set_parent_company')
        return action
