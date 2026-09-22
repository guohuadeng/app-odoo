# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import UserError


class ClearDataWizard(models.TransientModel):
    _name = 'clear.data.wizard'
    _description = 'Data Clear Scope Wizard'

    clear_scope = fields.Selection([
        ('global', 'All Companies'),
        ('company', 'Current Company Only'),
    ], string='Clear Scope', default='global', required=True)

    def action_confirm(self):
        self.ensure_one()
        clear_method = self.env.context.get('clear_method')
        if not clear_method:
            raise UserError(_('No clear method specified.'))
        settings = self.env['res.config.settings'].with_context(
            clear_scope=self.clear_scope
        )
        result = getattr(settings, clear_method)()
        if isinstance(result, dict):
            return result
        return {'type': 'ir.actions.client', 'tag': 'reload'}
