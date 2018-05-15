# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

# 限制时间,数据量不可太大
DAY_LIMIT = 30

class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    @api.multi
    def act_move_all_picking_open(self):
        self.ensure_one()
        picking_id = self.id
        stime = datetime.now() - timedelta(days=DAY_LIMIT)
        stime_str = stime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        if picking_id:
            action = self.env.ref('stock.stock_move_action').read()[0]
            action['name'] = "Stock Move All"
            action['domain'] = ['&', ('date_expected', '>', stime_str), ('picking_type_id', '=', picking_id)]
            action['context'] = {'search_default_done': True}
            return action

