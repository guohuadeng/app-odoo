# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class BaseModelExtend(models.AbstractModel):
    _name = 'basemodel.extend'
    _description = 'Base Extend for Sunpop'

    def _register_hook(self):
        '''
        Register method in BaseModel
        如果 该 fieldname 是m2o的，那么如果context没值，就用该模型第一个
        '''
        @api.model
        def _app_get_m2o_default(self, fieldname):
            if hasattr(self, fieldname) and self._fields[fieldname].type == 'many2one':
                if self._context.get(fieldname) or self._context.get('default_%s' % fieldname):
                    return self._context.get(fieldname) or self._context.get('default_%s' % fieldname)
                else:
                    rec = self.env[self._fields[fieldname].comodel_name].search([], limit=1)
                    return rec.id if rec else False
            return False

        models.BaseModel._app_get_default = _app_get_m2o_default
        return super(BaseModelExtend, self)._register_hook()
