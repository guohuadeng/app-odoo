# -*- coding: utf-8 -*-

import logging
import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
from odoo.osv import expression
_logger = logging.getLogger(__name__)


class Channel(models.Model):
    _inherit = 'discuss.channel'

    def get_openai_context(self, channel_id, author_id, answer_id, minutes=30, chat_count=0):
        gpt_id = False
        if self.ai_partner_id:
            ai_user = self.env['res.users'].search([('partner_id', '=', self.ai_partner_id.id)], limit=1)
            gpt_id = ai_user.mapped('gpt_id')
        if gpt_id and gpt_id.provider == 'deepseek':
            context_history = []
            afterTime = fields.Datetime.now() - datetime.timedelta(minutes=minutes)
            message_model = self.env['mail.message'].sudo()
            domain = [('res_id', '=', channel_id),
                  ('model', '=', 'discuss.channel'),
                  ('message_type', '!=', 'user_notification'),
                  ('parent_id', '!=', False),
                  ('is_ai', '=', True),
                  ('body', '!=', '<p>%s</p>' % _('Response Timeout, please speak again.')),
                  ('body', '!=', _('温馨提示：您发送的内容含有敏感词，请修改内容后再向我发送。'))]
            if self.channel_type in ['group', 'channel']:
                # 群聊增加时间限制，当前找所有人，不限制 author_id
                domain = expression.AND([domain, [('date', '>=', afterTime)]])
            else:
                domain = expression.AND([domain, [('author_id', '=', answer_id.id)]])
            if chat_count == 0:
                ai_msg_list = []
            else:
                ai_msg_list = message_model.with_context(tz='UTC').search(domain, order="id asc", limit=chat_count)
            for ai_msg in ai_msg_list:
                # 判断这个 ai_msg 是不是ai发，有才 insert。 判断 user_msg 是不是 user发的，有才 insert
                user_msg = ai_msg.parent_id.sudo()
                ai_content = str(ai_msg.body).replace("<p>", "").replace("</p>", "").replace("<p>", "")
                if ai_msg.author_id.sudo().gpt_id and answer_id.sudo().gpt_id and ai_msg.author_id.sudo().gpt_id == answer_id.sudo().gpt_id:
                    context_history.insert(0, {
                        'role': 'assistant',
                        'content': ai_content,
                    })
                if not user_msg.author_id.gpt_id:
                    user_content = user_msg.body.replace("<p>", "").replace("</p>", "").replace('@%s' % answer_id.name, '').lstrip()
                    context_history.append({
                        'role': 'user',
                        'content': user_content,
                    })
                    context_history.append({
                        'role': 'assistant',
                        'content': ai_content,
                    })
            return context_history
        else:
            return super(Channel, self).get_openai_context(channel_id, author_id, answer_id, minutes, chat_count)
