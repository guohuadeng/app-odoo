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
    _inherit = "res.partner"

    gpt_id = fields.Many2one('ai.robot', string='Bind to Ai', ondelete='set null')

    is_chat_private = fields.Boolean('Allow Chat Private', default=False)

    @api.model
    def im_search(self, name, limit=20, excluded_ids=None):
        users = self.env['res.users'].search([
            ('id', '!=', self.env.user.id),
            ('name', 'ilike', name),
            ('active', '=', True),
            ('share', '=', False),
            ('is_chat_private', '=', True)
        ], order='gpt_id, name, id', limit=limit)
        # return list(users.partner_id.mail_partner_format().values())
        return Store(users.partner_id).get_result()

    def mail_partner_format(self, fields=None):
        # TODO: remove !!!
        # 直接覆盖原生，增加 gpt_id 字段
        partners_format = dict()
        if not fields:
            fields = {'id': True, 'name': True, 'email': True, 'active': True, 'im_status': True, 'gpt_id': 0, 'user': {}}
        for partner in self:
            data = {}
            if 'id' in fields:
                data['id'] = partner.id
            if 'name' in fields:
                name = partner.name
                # 英文不好分，暂时不隐名
                # if not partner.related_user_id.gpt_id:
                #     name = partner.name[0] + '*' * (len(partner.name) - 1)
                data['name'] = name
            if 'email' in fields:
                data['email'] = partner.email
            if 'active' in fields:
                data['active'] = partner.active
            if 'im_status' in fields:
                data['im_status'] = partner.im_status
            if 'gpt_id' in fields:
                data['gpt_id'] = partner.gpt_id.id if partner.gpt_id else 0
            if 'user' in fields:
                internal_users = partner.user_ids - partner.user_ids.filtered('share')
                main_user = internal_users[0] if len(internal_users) > 0 else partner.user_ids[0] if len(partner.user_ids) > 0 else self.env['res.users']
                data['user'] = {
                    "id": main_user.id,
                    "isInternalUser": not main_user.share,
                } if main_user else [('clear',)]
            # if 'guest' in self.env.context or not self.env.user.has_group('base.group_erp_manager'):
            # 完全不显示 邮箱
            data.pop('email', None)
            partners_format[partner] = data
        return partners_format
