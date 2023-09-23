# -*- coding: utf-8 -*-

import openai
import requests, json
import datetime
# from transformers import TextDavinciTokenizer, TextDavinciModel
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.addons.app_common.models.base import get_ua_type

import logging
_logger = logging.getLogger(__name__)


class Channel(models.Model):
    _inherit = 'mail.channel'

    is_private = fields.Boolean(string="Private", default=False, help="Check to set Private, Can only use by user, not Public")
    # 因为 channel_member_ids 不好处理，在此增加此字段
    # 主Ai
    ai_partner_id = fields.Many2one(comodel_name="res.partner", string="Main Ai", required=False,
                                    domain=[('gpt_id', '!=', None), ('is_chat_private', '=', True)],
                                    default=lambda self: self._app_get_m2o_default('ai_partner_id'),
                                    help="Main Ai is the robot help you default.")
    ext_ai_partner_id = fields.Many2one(comodel_name="res.partner", string="Secondary Ai",
                                        domain=[('gpt_id', '!=', None), ('is_chat_private', '=', True)])
    description = fields.Char('Ai Character', help="Ai would help you act as the Character set.")
    set_max_tokens = fields.Selection([
        ('300', 'Short'),
        ('600', 'Standard'),
        ('1000', 'Medium'),
        ('2000', 'Long'),
        ('3000', 'Overlength'),
        ('32000', '32K'),
    ], string='Max Response', default='600', help="越大返回内容越多，计费也越多")
    set_chat_count = fields.Selection([
        ('none', 'Ai Auto'),
        ('1', '1标准'),
        ('3', '3强关联'),
        ('5', '5超强关联'),
    ], string="History Count", default='1', help="0-5，设定后，会将最近n次对话发给Ai，有助于他更好的回答，但太大费用也高")
    set_temperature = fields.Selection([
        ('2', '天马行空'),
        ('1.5', '创造性'),
        ('1', '标准'),
        ('0.6', '理性'),
        ('0.1', '保守'),
    ], string="Set Temperature", default='1', help="0-21，值越大越富有想像力，越小则越保守")
    set_top_p = fields.Selection([
        ('0.9', '严谨惯性思维'),
        ('0.6', '标准推理'),
        ('0.4', '跳跃性'),
        ('0.1', '随便'),
    ], string="Top Probabilities", default='0.6', help="0-1，值越大越倾向大众化的连贯思维")
    # 避免使用常用词
    set_frequency_penalty = fields.Selection([
        ('2', '老学究-晦涩难懂'),
        ('1.5', '学院派-较多高级词'),
        ('1', '标准'),
        ('0.1', '少常用词'),
        ('-1', '通俗易懂'),
        ('-2', '大白话'),
    ], string='Frequency Penalty', default='1', help="-2~2，值越大越少使用常用词")
    set_presence_penalty = fields.Selection([
        ('2', '多样强迫症'),
        ('1.5', '新颖化'),
        ('1', '标准'),
        ('0.1', '允许常规重复'),
        ('-1', '允许较多重复'),
        ('-2', '更多强调重复'),
    ], string='Presence penalty', default='1', help="-2~2，值越大越少重复词")

    # todo: 这里用 compute?
    max_tokens = fields.Integer('最长响应Token', default=600, help="越大返回内容越多，计费也越多")
    chat_count = fields.Integer(string="上下文数量", default=0, help="0~3，设定后，会将最近n次对话发给Ai，有助于他更好的回答")
    temperature = fields.Float(string="创造性值", default=1, help="0~2，值越大越富有想像力，越小则越保守")
    top_p = fields.Float(string="连贯性值", default=0.6, help="0~1，值越大越富有想像力，越小则越保守")
    frequency_penalty = fields.Float('避免常用词值', default=1, help="-2~2，值越大越少使用常用词")
    presence_penalty = fields.Float('避免重复词值', default=1, help="-2~2，值越大越少重复词")

    is_current_channel = fields.Boolean('是否当前用户默认频道', compute='_compute_is_current_channel', help='是否当前用户默认微信对话频道')

    def name_get(self):
        result = []
        for c in self:
            if c.channel_type == 'channel' and c.is_private:
                pre = '[私]'
            else:
                pre = ''
            result.append((c.id, "%s%s" % (pre, c.name or '')))
        return result

    def get_openai_context(self, channel_id, author_id, answer_id, minutes=60, chat_count=0):
        # 上下文处理，要处理群的方式，以及独聊的方式
        # azure新api 处理
        context_history = []
        afterTime = fields.Datetime.now() - datetime.timedelta(minutes=minutes)
        message_model = self.env['mail.message'].sudo()
        # 处理消息： 取最新问题 + 上 chat_count=1次的交互，将之前的交互按时间顺序拼接。
        # 注意： ai 每一次回复都有 parent_id 来处理连续性
        # 私聊处理

        # todo: 更好的处理方式
        domain = [('res_id', '=', channel_id),
                  ('model', '=', 'mail.channel'),
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
            ai_msg_list = message_model.with_context(tz='UTC').search(domain, order="id desc", limit=chat_count)
        for ai_msg in ai_msg_list:
            # 判断这个 ai_msg 是不是ai发，有才 insert。 判断 user_msg 是不是 user发的，有才 insert
            user_msg = ai_msg.parent_id.sudo()
            if ai_msg.author_id.sudo().gpt_id and answer_id.sudo().gpt_id and ai_msg.author_id.sudo().gpt_id == answer_id.sudo().gpt_id:
                ai_content = str(ai_msg.body).replace("<p>", "").replace("</p>", "").replace("<p>", "")
                context_history.insert(0, {
                    'role': 'assistant',
                    'content': ai_content,
                })
            if not user_msg.author_id.gpt_id:
                user_content = user_msg.description.replace("<p>", "").replace("</p>", "").replace('@%s' % answer_id.name, '').lstrip()
                context_history.insert(0, {
                    'role': 'user',
                    'content': user_content,
                })
        return context_history

    def get_ai_config(self, ai):
        # 勾子，用于取ai 配置
        return {}

    def get_ai_response(self, ai, messages, channel, user_id, message):
        author_id = message.create_uid.partner_id
        answer_id = user_id.partner_id
        # todo: 只有个人配置的群聊才给配置
        param = self.get_ai_config(ai)
        res, usage, is_ai = ai.get_ai(messages, author_id, answer_id, param)
        if res:
            if get_ua_type() != 'wxweb':
                # 处理当微信语音返回时，是直接回文本信息，不需要转换回车
                res = res.replace('\n', '<br/>')
            new_msg = channel.with_user(user_id).message_post(body=res, message_type='comment', subtype_xmlid='mail.mt_comment', parent_id=message.id)
            if usage:
                if ai.provider == 'ali':
                    prompt_tokens = usage['input_tokens']
                    completion_tokens = usage['output_tokens']
                    total_tokens = usage['input_tokens'] + usage['output_tokens']
                else:
                    prompt_tokens = usage['prompt_tokens']
                    completion_tokens = usage['completion_tokens']
                    total_tokens = usage['total_tokens']
                new_msg.write({
                    'human_prompt_tokens': prompt_tokens,
                    'ai_completion_tokens': completion_tokens,
                    'cost_tokens': total_tokens,
                })

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)
        # print(f'rdata:{rdata}')
        answer_id = self.env['res.partner']
        user_id = self.env['res.users']
        author_id = msg_vals.get('author_id')
        ai = self.env['ai.robot'].sudo()
        channel = self.env['mail.channel']
        channel_type = self.channel_type
        messages = []

        # 不处理 一般notify，但处理欢迎
        if '<div class="o_mail_notification' in message.body and message.body != _('<div class="o_mail_notification">joined the channel</div>'):
            return rdata
        if 'o_odoobot_command' in message.body:
            return rdata

        if channel_type == 'chat':
            channel_partner_ids = self.channel_partner_ids
            answer_id = channel_partner_ids - message.author_id
            user_id = answer_id.mapped('user_ids').sudo().filtered(lambda r: r.gpt_id)[:1]
            if user_id and answer_id.gpt_id:
                gpt_policy = user_id.gpt_policy
                gpt_wl_partners = user_id.gpt_wl_partners
                is_allow = message.author_id.id in gpt_wl_partners.ids
                if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
                    ai = answer_id.sudo().gpt_id

        elif channel_type in ['group', 'channel']:
            # partner_ids = @ ids
            partner_ids = list(msg_vals.get('partner_ids'))
            if hasattr(self, 'ai_partner_id') and self.ai_partner_id:
                # 当有主id时，使用主id
                if self.ai_partner_id.id in partner_ids:
                    partner_ids = [self.ai_partner_id.id]
            if partner_ids:
                # 常规群聊 @
                partners = self.env['res.partner'].search([('id', 'in', partner_ids)])
                # user_id = user, who has binded gpt robot
                user_id = partners.mapped('user_ids').sudo().filtered(lambda r: r.gpt_id)[:1]
            elif message.body == _('<div class="o_mail_notification">joined the channel</div>'):
                # 欢迎的情况
                partners = self.channel_partner_ids.sudo().filtered(lambda r: r.gpt_id)[:1]
                user_id = partners.mapped('user_ids')[:1]
            elif self.member_count == 2:
                # 处理独聊频道
                if hasattr(self, 'is_private') and not self.is_private:
                    # 2个人的非私有频道不处理
                    pass
                else:
                    partners = self.channel_partner_ids.sudo().filtered(lambda r: r.gpt_id and r != message.author_id)[:1]
                    user_id = partners.mapped('user_ids')[:1]
            elif not message.author_id.gpt_id:
                # 没有@时，默认第一个robot
                # robot = self.env.ref('app_chatgpt.chatgpt_robot')
                # 临时用azure
                if hasattr(self, 'ai_partner_id') and self.ai_partner_id:
                    # 当有主id时，使用主id
                    user_id = self.ai_partner_id.mapped('user_ids')[:1]
                else:
                    # 使用群里的第一个robot
                    partners = self.channel_partner_ids.sudo().filtered(lambda r: r.gpt_id)[:1]
                    user_id = partners.mapped('user_ids')[:1]
            if user_id:
                ai = user_id.sudo().gpt_id
            #     此处理不判断，将此处逻辑迁移至 get_ai_pre， 非ai回复的直接内容注意设置为 is_ai=false
            #     gpt_policy = user_id.gpt_policy
            #     gpt_wl_partners = user_id.gpt_wl_partners
            #     is_allow = message.author_id.id in gpt_wl_partners.ids
            #     answer_id = user_id.partner_id
            #     if gpt_policy == 'all' or (gpt_policy == 'limit' and is_allow):
            #         ai = user_id.sudo().gpt_id
            #     elif user_id.gpt_id and not is_allow:
            #         # 暂时有限用户的Ai
            #         raise UserError(_('此Ai暂时未开放，请联系管理员。'))
        if hasattr(ai, 'is_translator') and ai.is_translator:
            return rdata
        chatgpt_channel_id = self.env.ref('app_chatgpt.channel_chatgpt')
        
        if message.body == _('<div class="o_mail_notification">joined the channel</div>'):
            msg = _("Please warmly welcome our new partner %s and send him the best wishes.") % message.author_id.name
        else:
            # 不能用 preview， 如果用 : 提示词则 preview信息丢失
            plaintext_ct = tools.html_to_inner_content(message.body)
            msg = plaintext_ct.replace('@%s' % answer_id.name, '').lstrip()

        if not msg:
            return rdata

        if self._context.get('app_ai_sync_config') and self._context.get('app_ai_sync_config') in ['sync', 'async']:
            sync_config = self._context.get('app_ai_sync_config')
        else:
            sync_config = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openai_sync_config')
        # api_key = self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_api_key')
        # ai处理，不要自问自答
        if ai and answer_id != message.author_id:
            api_key = ai.openapi_api_key
            if not api_key:
                _logger.warning(_("ChatGPT Robot【%s】have not set open api key."))
                return rdata
            try:
                openapi_context_timeout = int(self.env['ir.config_parameter'].sudo().get_param('app_chatgpt.openapi_context_timeout')) or 60
            except:
                openapi_context_timeout = 60
            openai.api_key = api_key
            # 非4版本，取0次。其它取3 次历史
            chat_count = 3
            if '4' in ai.ai_model or '4' in ai.name:
                chat_count = 1
                if hasattr(self, 'chat_count'):
                    if self.chat_count > 0:
                        chat_count = 1
            else:
                chat_count = chat_count
                
            if author_id != answer_id.id and self.channel_type == 'chat':
                # 私聊
                _logger.info(f'私聊:author_id:{author_id},partner_chatgpt.id:{answer_id.id}')
                channel = self.env[msg_vals.get('model')].browse(msg_vals.get('res_id'))
            elif author_id != answer_id.id and msg_vals.get('model', '') == 'mail.channel' and msg_vals.get('res_id', 0) == chatgpt_channel_id.id:
                # todo: 公开的群聊，当前只开1个，后续更多
                _logger.info(f'频道群聊:author_id:{author_id},partner_chatgpt.id:{answer_id.id}')
                channel = chatgpt_channel_id
            elif author_id != answer_id.id and msg_vals.get('model', '') == 'mail.channel' and self.channel_type in ['group', 'channel']:
                # 高级用户自建的话题
                channel = self.env[msg_vals.get('model')].browse(msg_vals.get('res_id'))
                if hasattr(channel, 'is_private') and channel.description:
                    messages.append({"role": "system", "content": channel.description})
        
            try:
                c_history = self.get_openai_context(channel.id, author_id, answer_id, openapi_context_timeout, chat_count)
                if c_history:
                    messages += c_history
                messages.append({"role": "user", "content": msg})
                msg_len = sum(len(str(m)) for m in messages)
                # 接口最大接收 8430 Token
                if msg_len * 2 > ai.max_send_char:
                    messages = []
                    if hasattr(channel, 'is_private') and channel.description:
                        messages.append({"role": "system", "content": channel.description})
                    messages.append({"role": "user", "content": msg})
                    msg_len = sum(len(str(m)) for m in messages)
                    if msg_len * 2 > ai.max_send_char:
                        new_msg = channel.with_user(user_id).message_post(body=_('您所发送的提示词已超长。'), message_type='comment',
                                                                          subtype_xmlid='mail.mt_comment',
                                                                          parent_id=message.id)

                    # if msg_len * 2 >= 8000:
                    # messages = [{"role": "user", "content": msg}]
                if sync_config == 'sync':
                    self.get_ai_response(ai, messages, channel, user_id, message)
                else:
                    self.with_delay().get_ai_response(ai, messages, channel, user_id, message)
            except Exception as e:
                raise UserError(_(e))

        return rdata

    def _message_post_after_hook(self, message, msg_vals):
        if message.author_id.gpt_id:
            if msg_vals['body'] not in [_('Response Timeout, please speak again.'), _('温馨提示：您发送的内容含有敏感词，请修改内容后再向我发送。'),
                                        _('此Ai暂时未开放，请联系管理员。'), _('您所发送的提示词已超长。')]:
                message.is_ai = True
        return super(Channel, self)._message_post_after_hook(message, msg_vals)

    @api.model
    def _get_my_last_cid(self):
        # 获取当前用户最后一次进入的channel，返回该channel的id
        # todo: 优化，每次聊天进入时就 write
        user = self.env.user
        msgs = self.env['mail.message'].sudo().search([
            ('model', '=', 'mail.channel'),
            ('author_id', '=', user.partner_id.id),
        ], limit=3, order='id desc')
        c_id = 0
        c = self
        for m in msgs:
            c = self.browse(m.res_id)
            if c.is_member:
                c_id = c.id
                break
        if not c_id:
            c = self.env.ref('app_chatgpt.channel_chatgpt', raise_if_not_found=False)
            c_id = c.id or False
        if c and not c.is_member:
            c.sudo().add_members([user.partner_id.id])
        return c_id

    @api.onchange('ai_partner_id')
    def _onchange_ai_partner_id(self):
        if self.ai_partner_id and self.ai_partner_id.image_1920:
            self.image_128 = self.ai_partner_id.avatar_128
