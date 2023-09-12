# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    # todo: name 不能做多语种处理，使用高频，会太耗费性能
    # 注意 res.partner 是很特殊的，继承太多，故不能用 translate=True
    # name = fields.Char(translate=True)

    name_en_US = fields.Char('English Name')
    
    
