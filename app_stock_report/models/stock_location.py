# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

# 限制时间,数据量不可太大
DAY_LIMIT = 30

class StockLocation(models.Model):
    _inherit = "stock.location"

    day_limit = fields.Integer(string=u'Day limit in report dashboard', default=DAY_LIMIT)

    @api.multi
    def act_move_all_location_open(self):
        self.ensure_one()
        location_id = self.id
        stime = datetime.now() - timedelta(days=self.day_limit)
        stime_str = stime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        if location_id:
            action = self.env.ref('stock.stock_move_action').read()[0]
            action['name'] = "Stock Move All"
            action['domain'] = ['&', ('date_expected', '>', stime_str), '|', ('location_dest_id', '=', location_id), ('location_id', '=', location_id)]
            action['context'] = {'search_default_done': True}
            return action

    @api.multi
    def act_move_in_location_open(self):
        self.ensure_one()
        location_id = self.id
        stime = datetime.now() - timedelta(days=self.day_limit)
        stime_str = stime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        if location_id:
            action = self.env.ref('stock.stock_move_action').read()[0]
            action['name'] = "Stock Move In"
            action['domain'] = ['&', ('date_expected', '>', stime_str), ('location_dest_id', '=', location_id)]
            action['context'] = {'search_default_done': True}
            return action

    @api.multi
    def act_move_out_location_open(self):
        self.ensure_one()
        location_id = self.id
        stime = datetime.now() - timedelta(days=self.day_limit)
        stime_str = stime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        if location_id:
            action = self.env.ref('stock.stock_move_action').read()[0]
            action['name'] = "Stock Move Out"
            action['domain'] = ['&', ('date_expected', '>', stime_str), ('location_id', '=', location_id)]
            action['context'] = {'search_default_done': True}
            return action
