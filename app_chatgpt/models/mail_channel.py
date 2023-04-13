# -*- coding: utf-8 -*-

import openai
import requests, json
import datetime
# from transformers import TextDavinciTokenizer, TextDavinciModel
from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class Channel(models.Model):
    _inherit = 'mail.channel'
    
    def get_openai_context(self, channel_id, author_id, answer_id, minutes=30, chat_count=1):
        # 上下文处理，要处理群的方式，以及独聊的方式
        # azure新api 处理
        context_history = []
        afterTime = fields.Datetime.now() - datetime.timedelta(minutes=minutes)
        message_model = self.env['mail.message'].sudo()
        # 处理消息： 取最新问题 + 上 chat_count=1次的交互，将之前的交互按时间顺序拼接。
        # 注意： ai 每一次回复都有 parent_id 来处理连续性
        # 私聊处理
        domain = [('res_id', '=', channel_id),
                  ('model', '=', 'mail.channel'),
                  ('message_type', '!=', 'user_notification'),
                  ('parent_id', '!=', False),
                  ('author_id', '=', answer_id.id),
                  ('body', '!=', '<p>%s</p>' % _('Response Timeout, please speak again.'))]
        if self.channel_type in ['group', 'channel']:
            # 群聊增加时间限制，当前找所有人，不限制 author_id
            domain += [('date', '>=', afterTime)]
        ai_msg_list = message_model.with_context(tz='UTC').search(domain, order="id desc", limit=chat_count)
        for ai_msg in ai_msg_list:
            user_content = ai_msg.parent_id.description.replace("<p>", "").replace("</p>", "").replace('@%s' % answer_id.name, '').lstrip()
            ai_content = str(ai_msg.body).replace("<p>", "").replace("</p>", "").replace("<p>", "")
            context_history.insert(0, {
                'role': 'assistant',
                'content': ai_content,
            })
            context_history.insert(0, {
                'role': 'user',
                'content': user_content,
            })
        return context_history

    def get_ai_response(self, ai, messages, channel, user_id, message):
        author_id = message.create_uid.partner_id
        answer_id = user_id.partner_id
        res = ai.get_ai(messages, author_id, answer_id)
        if res:
            res = res.replace('\n', '<br/>')
            channel.with_user(user_id).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment', parent_id=message.id)

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        # print(f'rdata:{rdata}')
        answer_id = self.env['res.partner']
        user_id = self.env['res.users']
        author_id = msg_vals.get('author_id')
        ai = self.env['ai.robot']
        channel_type = self.channel_type
        if channel_type == 'chat':
            channel_partner_ids = self.channel_partner_ids
            answer_id = channel_partner_ids - message.author_id
            user_id = answer_id.mapped('user_ids').filtered(lambda r: r.gpt_id)[:1]
            if user_id and answer_id.gpt_id:
                gpt_policy = user_id.gpt_policy
                gpt_wl_users = user_id.gpt_wl_users
                is_allow = message.create_uid.id in gpt_wl_users.ids
                if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                    ai = answer_id.gpt_id

        elif channel_type in ['group', 'channel']:
            # partner_ids = @ ids
            partner_ids = list(msg_vals.get('partner_ids'))
            if partner_ids:
                partners = self.env['res.partner'].search([('id', 'in', partner_ids)])
                # user_id = user has binded gpt robot
                user_id = partners.mapped('user_ids').filtered(lambda r: r.gpt_id)[:1]
                if user_id:
                    gpt_policy = user_id.gpt_policy
                    gpt_wl_users = user_id.gpt_wl_users
                    is_allow = message.create_uid.id in gpt_wl_users.ids
                    answer_id = user_id.partner_id
                    if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                        ai = user_id.gpt_id

        chatgpt_channel_id = self.env.ref('app_chatgpt.channel_chatgpt')
        msg = message.description.replace('@%s' % answer_id.name, '').lstrip()
        
        # print('prompt:', prompt)
        # print('-----')
        if not msg:
            return rdata
        # api_key = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_api_key')
        api_key = ''
        if ai:
            api_key = ai.openapi_api_key
            if not api_key:
                _logger.warning(_("ChatGPT Robot【%s】have not set open api key."))
                return rdata
        try:
            openapi_context_timeout = int(self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_context_timeout')) or 60
        except:
            openapi_context_timeout = 60
        sync_config = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openai_sync_config')
        openai.api_key = api_key
        # print(msg_vals)
        # print(msg_vals.get('record_name', ''))
        # print('self.channel_type :',self.channel_type)
        if ai:
            # 非4版本，取0次。其它取3 次历史
            chat_count = 0 if '4' in ai.ai_model else 3
            if author_id != answer_id.id and self.channel_type == 'chat':
                # 私聊
                _logger.info(f'私聊:author_id:{author_id},partner_chatgpt.id:{answer_id.id}')
                channel = self.env[msg_vals.get('model')].browse(msg_vals.get('res_id'))
            elif author_id != answer_id.id and msg_vals.get('model', '') == 'mail.channel' and msg_vals.get('res_id', 0) == chatgpt_channel_id.id:
                # 公开的群聊
                _logger.info(f'频道群聊:author_id:{author_id},partner_chatgpt.id:{answer_id.id}')
                channel = chatgpt_channel_id
            elif author_id != answer_id.id and msg_vals.get('model', '') == 'mail.channel' and self.channel_type in ['group', 'channel']:
                # 其它群聊
                channel = self
        
            try:
                messages = [{"role": "user", "content": msg}]
                c_history = self.get_openai_context(channel.id, author_id, answer_id, openapi_context_timeout, chat_count)
                if c_history:
                    messages += c_history
                if sync_config == 'sync':
                    self.get_ai_response(ai, messages, channel, user_id, message)
                else:
                    self.with_delay().get_ai(ai, messages, channel, user_id, message)
            except Exception as e:
                raise UserError(_(e))

        return rdata

