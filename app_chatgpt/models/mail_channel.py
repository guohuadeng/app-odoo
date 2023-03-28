# -*- coding: utf-8 -*-

import openai
import requests,json
import datetime
# from transformers import TextDavinciTokenizer, TextDavinciModel
from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class Channel(models.Model):
    _inherit = 'mail.channel'

    @api.model
    def get_openai_context(self, channel_id, partner_chatgpt, current_prompt, seconds=600):
        afterTime = fields.Datetime.now() - datetime.timedelta(seconds=seconds)
        message_model = self.env['mail.message'].sudo()
        prompt = [f"Human:{current_prompt}\nAI:", ]
        domain = [('res_id', '=', channel_id),
                ('model', '=', 'mail.channel'),
                ('message_type', '!=', 'user_notification'),
                ('parent_id', '=', False),
                ('date', '>=', afterTime),
                ('author_id', '=', self.env.user.partner_id.id)]
        messages = message_model.with_context(tz='UTC').search(domain, order="id desc", limit=15)
        # print('domain:',domain)
        # print('messages:',messages)
        for msg in messages:
            ai_msg = message_model.search([("res_id", "=", channel_id),
                                           ('model', '=', msg.model),
                                           ('parent_id', '=', msg.id),
                                           ('author_id', '=', partner_chatgpt),
                                           ('body', '!=', '<p>获取结果超时，请重新跟我聊聊。</p>')])
            if ai_msg:
                prompt.append("Human:%s\nAI:%s" % (
                msg.body.replace("<p>", "").replace("</p>", ""), ai_msg.body.replace("<p>", "").replace("</p>", "")))
                # print(msg.body.replace("<p>", "").replace("</p>", ""))
                # print(ai_msg.body.replace("<p>", "").replace("</p>", ""))
            else:
                _logger.error(f"not find for id:{str(msg.id)}")

        return '\n'.join(prompt[::-1])

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        # print(f'rdata:{rdata}')
        to_partner_id = self.env['res.partner']
        user_id = self.env['res.users']
        author_id = msg_vals.get('author_id')
        ai = self.env['ai.robot']
        channel_type = self.channel_type
        if channel_type == 'chat':
            channel_partner_ids = self.channel_partner_ids
            to_partner_id = channel_partner_ids - message.author_id
            user_id = to_partner_id.mapped('user_ids').filtered(lambda r: r.gpt_id)[:1]
            if user_id:
                gpt_policy = user_id.gpt_policy
                gpt_wl_users = user_id.gpt_wl_users
                is_allow = message.create_uid.id in gpt_wl_users.ids
                if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                    ai = user_id.gpt_id

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
                    to_partner_id = user_id.partner_id
                    if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                        ai = user_id.gpt_id

        chatgpt_channel_id = self.env.ref('app_chatgpt.channel_chatgpt')

        prompt = msg_vals.get('body')
        # print('prompt:', prompt)
        # print('-----')
        if not prompt:
            return rdata
        # api_key = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_api_key')
        api_key = ''
        if ai:
            api_key = ai.openapi_api_key
            if not api_key:
                _logger.warning(_("ChatGPT Robot【%s】have not set open api key."))
                return rdata
        try:
            openapi_context_timeout = int(self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_context_timeout')) or 600
        except:
            openapi_context_timeout = 600

        openai.api_key = api_key
        partner_name = ''
        # print(msg_vals)
        # print(msg_vals.get('record_name', ''))
        # print('self.channel_type :',self.channel_type)
        if ai:
            if author_id != to_partner_id.id and self.channel_type == 'chat':
                _logger.info(f'私聊:author_id:{author_id},partner_chatgpt.id:{to_partner_id.id}')
                try:
                    channel = self.env[msg_vals.get('model')].browse(msg_vals.get('res_id'))
                    # if ai_model not in ['gpt-3.5-turbo', 'gpt-3.5-turbo-0301']:
                    prompt = self.get_openai_context(channel.id, to_partner_id.id, prompt, openapi_context_timeout)
                    print(prompt)
                    res = ai.get_ai(prompt, partner_name)
                    res = res.replace('\n', '<br/>')
                    # print('res:',res)
                    # print('channel:',channel)
                    channel.with_user(user_id).message_post(body=res, message_type='comment',subtype_xmlid='mail.mt_comment', parent_id=message.id)
                    # channel.with_user(user_chatgpt).message_post(body=res, message_type='notification', subtype_xmlid='mail.mt_comment')
                    # channel.sudo().message_post(
                    #     body=res,
                    #     author_id=partner_chatgpt.id,
                    #     message_type="comment",
                    #     subtype_xmlid="mail.mt_comment",
                    # )
                    # self.with_user(user_chatgpt).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment')
                except Exception as e:
                    raise UserError(_(e))
            elif author_id != to_partner_id.id and msg_vals.get('model', '') == 'mail.channel' and msg_vals.get('res_id', 0) == chatgpt_channel_id.id:
                _logger.info(f'频道群聊:author_id:{author_id},partner_chatgpt.id:{to_partner_id.id}')
                try:
                    prompt = self.get_openai_context(chatgpt_channel_id.id, to_partner_id.id, prompt, openapi_context_timeout)
                    res = ai.get_ai(prompt, 'odoo')
                    res = res.replace('\n', '<br/>')
                    chatgpt_channel_id.with_user(user_id).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment', parent_id=message.id)
                except Exception as e:
                    raise UserError(_(e))

        return rdata
