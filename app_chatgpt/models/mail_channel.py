# -*- coding: utf-8 -*-
# Copyright (c) 2020-Present InTechual Solutions. (<https://intechualsolutions.com/>)

import openai
import requests,json
import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)
class Channel(models.Model):
    _inherit = 'mail.channel'

    @api.model
    def get_openai(self, api_key, data, user="Odoo"):
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
        pdata = {
            "model": "text-davinci-003",
            "prompt": data,
            "temperature": 0.9,
            "max_tokens": 1000,
            "top_p": 1,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.6,
            "user": user,
            "stop": ["Human:", "AI:"]
        }
        response = requests.post("https://api.openai.com/v1/completions", data=json.dumps(pdata), headers=headers)
        res = response.json()
        if 'choices' in res:
            return '\n'.join([x['text'] for x in res['choices']])

        _logger.error(res)
        return "获取结果超时，请重新跟我聊聊。"

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

    def get_chatgpt_answer(self, prompt, partner_name):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.6,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            user=partner_name,
        )
        res = response['choices'][0]['text']
        return res

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        # print(f'rdata:{rdata}')

        chatgpt_channel_id = self.env.ref('app_chatgpt.channel_chatgpt')
        user_chatgpt = self.env.ref("app_chatgpt.user_chatgpt")
        partner_chatgpt = self.env.ref("app_chatgpt.partner_chatgpt")

        author_id = msg_vals.get('author_id')
        # print('author_id:',author_id)

        gpt_id = self.env['gpt.robot']
        partner_ids = list(msg_vals.get('partner_ids'))
        if partner_ids:
            partners = self.env['res.partner'].search([('id', 'in', partner_ids)])
            user_id = partners.mapped('user_ids').filtered(lambda r: r.gpt_id)[:1]
            if user_id:
                gpt_policy = user_id.gpt_policy
                gpt_wl_users = user_id.gpt_wl_users
                is_allow = message.create_uid.id in gpt_wl_users.ids
                if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                    user_chatgpt = user_id
                    partner_chatgpt = user_id.partner_id
                    gpt_id = user_id.gpt_id

        # print('partner_chatgpt.id:',partner_chatgpt.id)
        chatgpt_name = str(partner_chatgpt.name or '') + ', '
        # print('chatgpt_name:', chatgpt_name)
        prompt = msg_vals.get('body')
        # print('prompt:', prompt)
        # print('-----')
        if not prompt:
            return rdata
        api_key = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_api_key')
        if gpt_id:
            api_key = gpt_id.openapi_api_key
        try:
            openapi_context_timeout = int(self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_context_timeout')) or 600
        except:
            openapi_context_timeout = 600

        openai.api_key = api_key
        Partner = self.env['res.partner']
        partner_name = ''
        if author_id:
            partner_id = Partner.browse(author_id)
            if partner_id:
                user_id = partner_id.user_ids[:1]
                if user_id.gpt_id:
                    return rdata
                partner_name = partner_id.name
        # print(msg_vals)
        # print(msg_vals.get('record_name', ''))
        # print('self.channel_type :',self.channel_type)
        if author_id != partner_chatgpt.id and (chatgpt_name in msg_vals.get('record_name', '') or 'ChatGPT,' in msg_vals.get('record_name', '') ) and self.channel_type == 'chat':
            _logger.info(f'私聊:author_id:{author_id},partner_chatgpt.id:{partner_chatgpt.id}')
            try:
                channel = self.env[msg_vals.get('model')].browse(msg_vals.get('res_id'))
                prompt = self.get_openai_context(channel.id, partner_chatgpt.id, prompt,openapi_context_timeout)
                print(prompt)
                # res = self.get_chatgpt_answer(prompt,partner_name)
                res = self.get_openai(api_key, prompt, partner_name)
                # print('res:',res)
                # print('channel:',channel)
                channel.with_user(user_chatgpt).message_post(body=res, message_type='comment',subtype_xmlid='mail.mt_comment',parent_id=message.id)
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

        elif author_id != partner_chatgpt.id and msg_vals.get('model', '') == 'mail.channel' and msg_vals.get('res_id', 0) == chatgpt_channel_id.id:
            _logger.info(f'频道群聊:author_id:{author_id},partner_chatgpt.id:{partner_chatgpt.id}')
            try:
                prompt = self.get_openai_context(chatgpt_channel_id.id, partner_chatgpt.id, prompt,openapi_context_timeout)
                # print(prompt)
                # res = self.get_chatgpt_answer(prompt, partner_name)
                res = self.get_openai(api_key, prompt, partner_name)
                chatgpt_channel_id.with_user(user_chatgpt).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment',parent_id=message.id)
            except Exception as e:
                raise UserError(_(e))

        return rdata
