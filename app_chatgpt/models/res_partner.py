# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    gpt_id = fields.Many2one('ai.robot', string='Bind to ChatGpt')
