# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp

import logging

logger = logging.getLogger(__name__)


class Picking(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking', 'barcodes.barcode_events_mixin']

    # 是否在扫码视图，暂时不用，使用原生方式处理
    is_barcode_view = fields.Boolean('Barcode view', defult=False)
    # 扫码摘要
    header_title = fields.Char('Briefing', compute='_compute_briefing')

    pack_operation_product_current_ids = fields.One2many(
        'stock.pack.operation', 'picking_id', string='Product packing',
        compute='_compute_product_current', readonly=True, copy=False)
    # 作业,已装入包操作的散件
    pack_operation_product_packed_ids = fields.One2many(
        'stock.pack.operation', 'picking_id', string='Product packed',
        domain=[('product_id', '>=', 1), ('qty_done', '>=', 1), ('result_package_id', '!=', False)], readonly=True, copy=False)
    # 散件涉及到的包裹列表
    result_package_ids = fields.Many2many('stock.quant.package', string='Result Packages', readonly=True, copy=False)
    # 上次操作产品
    last_op_product = fields.Many2one('product.product', string='Last OP', readonly=True, copy=False)
    # 上次打包的包裹，用于批量克隆
    last_op_package = fields.Many2one('stock.quant.package', string='Last Package', readonly=True, copy=False)

    # 待办统计，散件与包裹一起处理的数量
    product_qty_total = fields.Float('To Do Total', compute="_compute_product_qty_total",
                                     digits=dp.get_precision('Product Unit of Measure'), readonly=True, store=True)  # 总待办数量
    package_count = fields.Integer('Package Total', compute="_compute_package_count", readonly=True)  # 待处理的包裹数量
    # 完成统计，验证后才有
    qty_done_total = fields.Float('Done Total', compute="_compute_done_total",
                                  digits=dp.get_precision('Product Unit of Measure'), readonly=True, store=True, copy=False)  # 总完成数量
    weight_done_total = fields.Float('Weight Done Total(kg)', digits=dp.get_precision('Stock Weight'),
                                     compute="_compute_done_total", readonly=True, store=True, copy=False)  # 总完成重量
    package_done_count = fields.Integer('Package Done Total', compute="_compute_package_done_count", readonly=True, store=True, copy=False)  # 已处理的包裹数量
    result_package_count = fields.Integer('Result Package Total', compute="_compute_package_done_count", readonly=True, store=True, copy=False)  # 放入的包裹数量

    @api.depends('partner_id')
    def _compute_briefing(self):
        for rec in self:
            try:
                title = '客户:' + rec.partner_id.name
                if rec.origin:
                    title += '，源单据：' + rec.origin
                rec.header_title = title
            except:
                pass

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

    @api.multi
    @api.depends('pack_operation_product_ids.result_package_id', 'pack_operation_pack_ids')
    def _compute_package_count(self):
        for rec in self:
            # 散件打包数量
            rec.package_count = len(rec.pack_operation_product_packed_ids.mapped('result_package_id').ids)
            # 包裹再打包数量
            rec.package_count += len(rec.pack_operation_pack_ids)

    @api.multi
    @api.depends('state', 'pack_operation_product_ids.result_package_id', 'pack_operation_pack_ids.result_package_id')
    def _compute_package_done_count(self):
        for rec in self:
            if rec.state == 'done':
                rec.result_package_count = len(rec.pack_operation_product_packed_ids.mapped('result_package_id').ids)
                pack_packs = rec.pack_operation_pack_ids.filtered(lambda pack: not pack.product_id and pack.qty_done and pack.result_package_id)
                rec.package_done_count += len(pack_packs.mapped('result_package_id').ids) + rec.result_package_count

    # 不用于字段compute，在每次放入包裹操作执行，重新计算
    # 设置上次打包的包裹
    @api.multi
    def set_package(self, pack):
        for rec in self:
            if pack:
                rec.last_op_package = pack
            if rec.pack_operation_product_packed_ids:
                rec.result_package_ids = rec.pack_operation_product_ids.mapped('result_package_id').ids
            rec.package_count = len(rec.result_package_ids) + len(rec.pack_operation_pack_ids)
        pass

    @api.multi
    def put_in_pack(self):
        pack = super(Picking, self).put_in_pack()
        self.set_package(pack)
        return pack

    @api.multi
    @api.depends('pack_operation_product_ids.qty_done', 'state')
    def _compute_product_current(self):
        for op in self:
            if op.pack_operation_product_ids and op.state == 'assigned':
                op.pack_operation_product_current_ids = op.pack_operation_product_ids.filtered(
                    lambda x: x.product_id and x.qty_done >= 1 and not x.result_package_id)

    def action_see_packages(self):
        self.ensure_one()
        action = self.env.ref('stock.action_package_view').read()[0]
        packages = self.pack_operation_product_ids.mapped('result_package_id')
        packages += self.pack_operation_pack_ids.mapped('result_package_id')
        action['domain'] = [('id', 'in', packages.ids)]
        return action

