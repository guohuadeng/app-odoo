# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

import requests
import base64
from io import BytesIO

from datetime import date, datetime, time
import pytz

import logging

_logger = logging.getLogger(__name__)

# 常规的排除的fields
EXCLU_FIELDS = [
    '__last_update',
    'access_token',
    'access_url',
    'access_warning',
    'activity_date_deadline',
    'activity_exception_decoration',
    'activity_exception_icon',
    'activity_ids',
    'activity_state',
    'activity_summary',
    'activity_type_id',
    'activity_user_id',
    'display_name',
    'message_attachment_count',
    'message_channel_ids',
    'message_follower_ids',
    'message_has_error',
    'message_has_error_counter',
    'message_has_sms_error',
    'message_ids',
    'message_is_follower',
    'message_main_attachment_id',
    'message_needaction',
    'message_needaction_counter',
    'message_partner_ids',
    'message_unread',
    'message_unread_counter',
    'website_message_ids',
    'write_date',
    'write_uid',
]


class Base(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def _get_normal_fields(self):
        f_list = []
        for k, v in self._fields.items():
            if k not in EXCLU_FIELDS:
                f_list.append(k)
        return f_list

    @api.model
    def _app_get_m2o_default(self, fieldname, domain=[]):
        if hasattr(self, fieldname) and self._fields[fieldname].type == 'many2one':
            if self._context.get(fieldname) or self._context.get('default_%s' % fieldname):
                return self._context.get(fieldname) or self._context.get('default_%s' % fieldname)
            else:
                rec = self.env[self._fields[fieldname].comodel_name].sudo().search(domain, limit=1)
                return rec.id if rec else False
        return False

    def _app_dt2local(self, value, return_format=DEFAULT_SERVER_DATETIME_FORMAT):
        """
        将value中时间，按格式转为用户本地时间.注意只处理in str为字符串类型,如果是时间类型直接用 datetime.now(tz)
        """
        if not value:
            return value
        if isinstance(value, datetime):
            value = value.strftime(return_format)
        dt = datetime.strptime(value, return_format)
        user_tz = pytz.timezone(self.env.user.tz or 'Etc/GMT-8')
        _logger.warning('============= user2 tz: %s' % user_tz)
        dt = dt.replace(tzinfo=pytz.timezone('UTC'))
        return dt.astimezone(user_tz).strftime(return_format)

    def _app_dt2utc(self, value, return_format=DEFAULT_SERVER_DATETIME_FORMAT):
        """
        将value中用户本地时间，按格式转为UTC时间，输出 str
        """
        if not value:
            return value
        if isinstance(value, datetime):
            value = value.strftime(return_format)
        dt = datetime.strptime(value, return_format)
        pytz_timezone = pytz.timezone('Etc/GMT+8')
        dt = dt.replace(tzinfo=pytz.timezone('UTC'))
        return dt.astimezone(pytz_timezone).strftime(return_format)

    @api.model
    def get_image_from_url(self, url):
        if not url:
            return None
        try:
            response = requests.get(url)  # 将这个图片保存在内存
        except Exception as e:
            return None
        # 返回这个图片的base64编码
        return base64.b64encode(BytesIO(response.content).read())
