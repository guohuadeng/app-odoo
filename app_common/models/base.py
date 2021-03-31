# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

from datetime import date, datetime, time
import pytz

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

    def _app_dt2local(self, value, return_format=DEFAULT_SERVER_DATETIME_FORMAT):
        """
        将value中时间，按格式转为用户本地时间
        """
        if not value:
            return value
        if isinstance(value, datetime):
            value = value.strftime(return_format)
        dt = datetime.strptime(value, return_format)
        pytz_timezone = pytz.timezone(self.env.user.tz or 'Etc/GMT-8')
        dt = dt.replace(tzinfo=pytz.timezone('UTC'))
        return dt.astimezone(pytz_timezone).strftime(return_format)

    def _app_dt2utc(self, value, return_format=DEFAULT_SERVER_DATETIME_FORMAT):
        """
        将value中用户本地时间，按格式转为UTC时间，输出 str
        """
        if not value:
            return value
        if isinstance(value, datetime):
            value = value.strftime(return_format)
        dt = datetime.strptime(value, return_format)
        user_tz = pytz.timezone(self.env.user.tz or 'Etc/GMT+8')
        dt = dt.replace(tzinfo=pytz.timezone('UTC'))
        return dt.astimezone(user_tz).strftime(return_format)
