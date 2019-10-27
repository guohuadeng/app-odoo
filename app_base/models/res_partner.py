# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import collections
import datetime
import hashlib
import pytz
import threading
import re

from email.utils import formataddr

import requests
from lxml import etree
from werkzeug import urls

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.modules import get_module_resource
from odoo.osv.expression import get_unaccent_wrapper
from odoo.exceptions import UserError, ValidationError
from odoo.tools import pycompat


class Partner(models.Model):
    _inherit = 'res.partner'

    def _get_default_customer(self):
        search_partner_mode = self.env.context.get('res_partner_search_mode')
        is_customer = search_partner_mode == 'customer'
        if is_customer and not self.env.context.get('default_customer'):
            return is_customer
        else:
            return None

    def _get_default_supplier(self):
        search_partner_mode = self.env.context.get('res_partner_search_mode')
        is_supplier = search_partner_mode == 'supplier'
        if is_supplier and not self.env.context.get('default_supplier'):
            return is_supplier
        else:
            return None

    customer = fields.Boolean(string='Is a Customer', default=_get_default_customer, inverse='_set_customer',
                               help="Check this box if this contact is a customer. It can be selected in sales orders.")
    supplier = fields.Boolean(string='Is a Vendor', default=_get_default_supplier, inverse='_set_supplier',
                               help="Check this box if this contact is a vendor. It can be selected in purchase orders.")

    def _set_customer(self):
        for rec in self:
            if rec.customer:
                if rec.customer_rank < 1 or not rec.customer_rank:
                    rec.customer_rank = 1
            else:
                rec.customer_rank = 0

    def _set_supplier(self):
        for rec in self:
            if rec.supplier:
                if rec.supplier_rank < 1 or not rec.supplier_rank:
                    rec.supplier_rank = 1
            else:
                rec.supplier_rank = 0

