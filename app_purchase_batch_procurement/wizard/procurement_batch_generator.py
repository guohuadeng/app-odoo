# -*- encoding: utf-8 -*-


from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import Warning
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ProcurementBatchGenerator(models.TransientModel):
    _name = 'procurement.batch.generator'
    _description = 'Wizard to create procurements from product tree'

    route_ids = fields.Many2many('stock.location.route', string='Preferred Routes')
    line_ids = fields.One2many(
        'procurement.batch.generator.line', 'parent_id',
        string='Procurement Request Lines')

    @api.model
    def default_get(self, fields):
        res = super(ProcurementBatchGenerator, self).default_get(fields)
        assert isinstance(self.env.context['active_ids'], list),\
            "context['active_ids'] must be a list"
        line_ids = []
        warehouses = self.env['stock.warehouse'].search(
            [('company_id', '=', self.env.user.company_id.id)])
        warehouse_id = warehouses and warehouses[0].id or False
        # product.template是被继承的，所以用同样方法即可
        for product in self.env['product.product'].browse(
                self.env.context['active_ids']):
            # todo: 库存的数量在此使用会导致运算量较大，停用。 如需要再加。未来可以考虑数据全部从前端送过来，不需再查数据库
            # partner_id = product.seller_ids and product.seller_ids[0].id or False
            if product.virtual_available < 0:
                procurement_qty = product.virtual_available * -1
            else:
                procurement_qty = 1
            line_ids.append([0, 0, {
                'name': product.name,
                'product_id': product.id,
                # 'partner_id': partner_id,
                # 'qty_available': product.qty_available,
                'virtual_available': product.virtual_available,
                # 'outgoing_qty': product.outgoing_qty,
                # 'incoming_qty': product.incoming_qty,
                'uom_id': product.uom_id.id,
                # 按预测库存数补货，or 1
                'procurement_qty': procurement_qty,
                'warehouse_id': warehouse_id,
                'date_planned': datetime.now().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                }])
        try:
            res.update({
                'line_ids': line_ids,
            })
        except:
            pass
        return res

    @api.multi
    def validate(self):
        self.ensure_one()
        wiz = self[0]
        assert wiz.line_ids, 'wizard must have some lines'
        procs = self.env['procurement.order']
        for line in wiz.line_ids:
            if not line.procurement_qty:
                continue
            procurement = self.env['procurement.order'].create(
                line._prepare_procurement_order())
            procs += procurement
        if not procs.ids:
            raise Warning(_('All requested quantities are null.'))
        # todo: 看是否需要记录工作流
        # self.pool['procurement.order'].signal_workflow(
        #     self._cr, self._uid, new_po_ids, 'button_confirm')
        # todo: 看是用 self.pool还是直接run，当前用直接run
        # self.pool['procurement.order'].run(
        #     self._cr, self._uid, new_po_ids, context=self.env.context)
        procs.run()
        action = self.env.ref('procurement.procurement_action').read()[0]
        action['domain'] = [('id', 'in', procs.ids)]
        return action

class ProcurementBatchGeneratorLine(models.TransientModel):
    _name = 'procurement.batch.generator.line'
    _description = 'Lines of the wizard to request procurements'

    parent_id = fields.Many2one(
        'procurement.batch.generator', string='Parent')
    product_id = fields.Many2one(
        'product.product', string='Product', readonly=True)
    partner_id = fields.Many2one(
        'res.partner', string='Supplier', required=False)
    qty_available = fields.Float(
        string='Quantity On Hand',
        digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    virtual_available = fields.Float(
        string='Forecast Quantity',
        digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    outgoing_qty = fields.Float(
        string='Incoming Quantity',
        digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    incoming_qty = fields.Float(
        string='Outgoing Quantity',
        digits=dp.get_precision('Product Unit of Measure'), readonly=True)
    procurement_qty = fields.Float(
        string='Requested Quantity',
        digits=dp.get_precision('Product Unit of Measure'), default=1)
    uom_id = fields.Many2one(
        'product.uom', string='Unit of Measure', readonly=True)
    warehouse_id = fields.Many2one(
        'stock.warehouse', string='Warehouse')
    date_planned = fields.Datetime(string='Planned Date')

    @api.multi
    def _prepare_procurement_order(self):
        self.ensure_one()
        vals = {
            'name': 'INT: %s' % (self.env.user.login),
            'date_planned': self.date_planned,
            'product_id': self.product_id.id,
            'product_qty': self.procurement_qty,
            'product_uom': self.uom_id.id,
            'location_id': self.warehouse_id.lot_stock_id.id,
            'company_id': self.warehouse_id.company_id.id,
            'route_ids': [(6, 0, self.parent_id.route_ids.ids)],
            }
        return vals
