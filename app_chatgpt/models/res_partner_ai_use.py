# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartnerAiUse(models.Model):
    _name = "res.partner.ai.use"
    _description = '消费者Ai使用情况'

    name = fields.Many2one('res.partner', 'Partner')
    ai_user_id = fields.Many2one('res.users', 'Ai User', domain=[('gpt_id', '!=', False)])
    first_ask_time = fields.Datetime('First Ask Time')
    latest_ask_time = fields.Datetime('Latest Ask Time')
    service_start_date = fields.Datetime('Service Start Date')
    service_end_date = fields.Datetime('Service End Date')
    used_number = fields.Integer('Number of Used')
    max_number = fields.Integer('Max Number of Call')
    human_prompt_tokens = fields.Integer('Human Prompt Tokens')
    ai_completion_tokens = fields.Integer('AI Completion Tokens')
    tokens_total = fields.Integer('Total Tokens')
    token_balance = fields.Integer('Token Balance')
    # balance = allow - total
    token_allow = fields.Integer('Token Allow')

