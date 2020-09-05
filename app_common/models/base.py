# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Base(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def _app_get_m2o_default(self, fieldname, domain=[]):
        if hasattr(self, fieldname) and self._fields[fieldname].type == 'many2one':
            if self._context.get(fieldname) or self._context.get('default_%s' % fieldname):
                return self._context.get(fieldname) or self._context.get('default_%s' % fieldname)
            else:
                rec = self.env[self._fields[fieldname].comodel_name].search(domain, limit=1)
                return rec.id if rec else False
        return False
