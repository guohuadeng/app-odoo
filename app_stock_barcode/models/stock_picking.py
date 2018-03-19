# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp

import logging

logger = logging.getLogger(__name__)


class Picking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'barcodes.barcode_events_mixin']

    # 作业,已扫码未装入包操作的记录行
    pack_operation_product_current_ids = fields.One2many(
        'stock.pack.current', 'picking_id', string='Product packing', readonly=True, copy=False)
    # 作业,已装入包操作的散件
    pack_operation_product_packed_ids = fields.One2many(
        'stock.pack.operation', 'picking_id', 'Product packed',
        domain=[('product_id', '>=', 1), ('qty_done', '>=', 1), ('result_package_id', '!=', False)], readonly=True, copy=False)
    # 散件涉及到的包裹列表
    result_package_ids = fields.Many2many('stock.quant.package', string='Relate Packages', readonly=True, copy=False)
    # 当前操作产品
    last_op_product = fields.Many2one('product.product', string='Last OP', readonly=True)

    # 统计，散件与包裹一起处理的数量
    product_qty_total = fields.Float('To Do Total', compute="_compute_product_qty_total",
                                     digits=dp.get_precision('Product Unit of Measure'), readonly=True, store=True)  # 总待办数量
    qty_done_total = fields.Float('Done Total', compute="_compute_done_total",
                                  digits=dp.get_precision('Product Unit of Measure'), readonly=True, store=True)  # 总完成数量
    weight_done_total = fields.Float('Weight Done Total(kg)', digits=dp.get_precision('Stock Weight'),
                                     compute="_compute_done_total", readonly=True, store=True)  # 总完成重量
    package_count = fields.Integer('Package Total', compute="_compute_package_count",  readonly=True)  # 待处理的包裹数量
    package_done_count = fields.Integer('Package Done Total', compute="_compute_package_done_count", readonly=True, store=True)  # 已处理的包裹数量

    @api.depends('pack_operation_product_ids.product_qty', 'pack_operation_pack_ids.product_qty')
    def _compute_product_qty_total(self):
        for rec in self:
            try:
                rec.product_qty_total = sum(rec.pack_operation_product_ids.mapped('product_qty'))
                rec.product_qty_total += sum(rec.pack_operation_pack_ids.filtered(lambda pack: not pack.is_done).mapped('package_id.qty_done_total'))
            except:
                rec.product_qty_total = 0

    @api.depends('pack_operation_product_ids.qty_done', 'pack_operation_pack_ids.qty_done')
    def _compute_done_total(self):
        for rec in self:
            # 此处用一次遍历减少计算量
            qty_done_total = 0
            weight_done_total = 0
            for op in rec.pack_operation_product_ids:
                qty_done_total += op.qty_done
                try:
                    weight_op = op.product_id.weight * op.qty_done
                except:
                    weight_op = 0
                weight_done_total += weight_op
            # qty_done_total += sum(rec.pack_operation_pack_ids.mapped('package_id.qty_done_total'))
            weight_done_total += sum(rec.pack_operation_pack_ids.filtered(lambda pack: pack.qty_done).mapped('package_id.weight_done_total'))
            rec.qty_done_total = qty_done_total
            rec.weight_done_total = weight_done_total

    @api.depends('pack_operation_product_ids.result_package_id', 'pack_operation_pack_ids')
    @api.one
    def _compute_package_count(self):
        for rec in self:
            # 散件打包数量
            rec.package_count = len(rec.pack_operation_product_packed_ids.mapped('result_package_id').ids)
            # 包裹再打包数量
            rec.package_count += len(rec.pack_operation_pack_ids)

    @api.depends('state', 'pack_operation_product_ids.result_package_id', 'pack_operation_pack_ids.result_package_id')
    @api.one
    def _compute_package_done_count(self):
        for rec in self:
            if rec.state == 'done':
                rec.package_done_count = len(rec.pack_operation_product_packed_ids.mapped('result_package_id').ids)
                pack_packs = rec.pack_operation_pack_ids.filtered(lambda pack: not pack.product_id and pack.qty_done and pack.result_package_id)
                rec.package_done_count += len(pack_packs.mapped('result_package_id').ids)


    # 不用于字段compute，在每次放入包裹操作执行，重新计算
    def set_package(self):
        for rec in self:
            if rec.pack_operation_product_packed_ids:
                rec.result_package_ids = rec.pack_operation_product_ids.mapped('result_package_id').ids
            rec.package_count = len(rec.result_package_ids) + len(rec.pack_operation_pack_ids)
        pass

    @api.multi
    def put_in_pack2(self):
        self.put_in_pack()

    @api.multi
    def put_in_pack(self):
        pack = super(Picking, self).put_in_pack()
        self.set_package()
        self.set_current()
        return pack

    # 每次重新算，todo: 只更新相关行
    @api.onchange('pack_operation_product_ids')
    def set_current(self):
        self.pack_operation_product_current_ids = [(5, 0, 0)]
        current_ids = []
        if self.pack_operation_product_ids and self.state != 'done':
            current_ids = self.pack_operation_product_ids \
                .filtered(lambda pack: pack.product_id and pack.qty_done > 0 and not pack.result_package_id)
        if current_ids:
            ops = []
            for op in current_ids:
                ops.insert(0, [0, 0, {
                    'picking_id': self.id,
                    'product_id': op.product_id.id,
                    'product_uom_id': op.product_uom_id.id,
                    'product_qty': op.product_qty,
                    'qty_done': op.qty_done,
                    'weight': op.weight,
                }])
            self.update({'pack_operation_product_current_ids': ops})

    def _check_product(self, product, qty=1.0):
        self.last_op_product = product
        return super(Picking, self)._check_product()