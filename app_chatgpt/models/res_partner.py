# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2009-TODAY odooai.cn Ltd.(广州欧度智能科技有限公司) https://www.odooai.cn
#    Author: Ivan Deng，ivan@odooai.cn   300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.

#    Create on 2024-10-06
##############################################################################

from odoo import fields, models, api
from odoo.addons.mail.tools.discuss import Store


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gpt_id = fields.Many2one('ai.robot', string='Bind to Ai', ondelete='set null')

    is_chat_private = fields.Boolean('Allow Chat Private', default=False)

    @api.model
    def im_search(self, name, limit=20, excluded_ids=None):
        # Odoo20: core 已无 im_search / Store(records).get_result()，改用新 Store().add() API
        users = self.env['res.users'].search([
            ('id', '!=', self.env.user.id),
            ('name', 'ilike', name),
            ('active', '=', True),
            ('share', '=', False),
            ('is_chat_private', '=', True)
        ], order='gpt_id, name, id', limit=limit)
        store = Store().add(users.partner_id, "_store_partner_fields")
        return store.as_dict()

    def _store_partner_fields(self, res):
        # Odoo20: 原 mail_partner_format 覆盖已废弃，改为扩展 Store 字段方法，增加 gpt_id
        super()._store_partner_fields(res)
        res.attr("gpt_id", lambda p: p.gpt_id.id if p.gpt_id else 0)
