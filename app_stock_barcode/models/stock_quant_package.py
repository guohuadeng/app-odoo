# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError

class QuantPackage(models.Model):
    _inherit = 'stock.quant.package'
    qty_done_total = fields.Float('Done Total', default=0.0, store=True,
                                  compute="_compute_done_total",
                                  digits=dp.get_precision('Product Unit of Measure'))  # 总完成数量
    weight_done_total = fields.Float('Weight Done Total(kg)', default=0, store=True,
                                     digits=dp.get_precision('Stock Weight'),
                                     compute="_compute_done_total", readonly=True)  # 总完成重量

    @api.depends('quant_ids.qty')
    def _compute_done_total(self):
        for rec in self:
            try:
                rec.qty_done_total = sum(rec.quant_ids.mapped('qty'))
            except:
                rec.qty_done_total = 0
            try:
                rec.weight_done_total = sum(rec.quant_ids.mapped('weight_done_subtotal'))
            except:
                rec.weight_done_total = 0

    def _compute_complete_name(self):
        """ Forms complete name of location from parent location to child location. """
        res = {}
        for package in self:
            current = package
            name = current.name
            while current.parent_id:
                name = '%s / %s' % (current.parent_id.name, name)
                current = current.parent_id

            if package.qty_done_total>0:
                name += '-[%spcs]' % (str(package.qty_done_total))
            if package.weight_done_total>0:
                name += '-[%skg]' % (str(package.weight_done_total))

            res[package.id] = name
        return res