# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ForceSetParentCompany(models.TransientModel):
    _name = 'force.set.parent.company'
    _description = 'Force Set Parent Company'

    company_id = fields.Many2one('res.company', string='Company', required=True)
    target_parent_company_id = fields.Many2one('res.company', string='Parent Company', required=True, domain="[('id', '!=', company_id)]")

    @api.model
    def default_get(self, fields):
        res = super(ForceSetParentCompany, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        res['company_id'] = active_id
        return res

    def action_confirm(self):
        self.ensure_one()
        if not self:
            return
        self.env.cr.execute("""
            UPDATE res_company
            SET parent_id = %s
            WHERE id = %s
        """, (self.target_parent_company_id.id, self.company_id.id))
        self.company_id._parent_store_compute()
        self.env.registry.clear_cache()
