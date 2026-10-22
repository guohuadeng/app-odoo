# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _app_is_stop_subscribe(self):
        """ 读取系统参数，判断是否停用订阅/关注及 bus 实时推送。 """
        return self.env['ir.config_parameter'].sudo().get_str('app_stop_subscribe', '') == "True"

    def message_subscribe(self, partner_ids=None, subtype_ids=None):
        """ 停用订阅功能。签名与 Odoo 20 核心一致（核心已移除 channel_ids）。 """
        if self._app_is_stop_subscribe():
            return True
        return super().message_subscribe(partner_ids, subtype_ids)

    def _message_subscribe(self, partner_ids=None, subtype_ids=None, customer_ids=None):
        """ 停用订阅功能. """
        if self._app_is_stop_subscribe():
            return True
        return super()._message_subscribe(partner_ids, subtype_ids, customer_ids)

    def _message_auto_subscribe_followers(self, updated_values, default_subtype_ids):
        """ 停用订阅功能. """
        if self._app_is_stop_subscribe():
            return []
        return super()._message_auto_subscribe_followers(updated_values, default_subtype_ids)

    def _message_auto_subscribe_notify(self, partner_ids, template):
        """ 停用订阅功能. """
        if self._app_is_stop_subscribe():
            return True
        return super()._message_auto_subscribe_notify(partner_ids, template)
