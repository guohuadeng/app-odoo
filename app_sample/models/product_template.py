# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.

#    Create on 2023-10-06
##############################################################################

from odoo import models, fields, api, _
from odoo.tools.translate import html_translate

import logging
_logger = logging.getLogger(__name__)

# Template for model inherit
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    short_name = fields.Char(string='Short Name', translate=True, readonly=False, copy=True)