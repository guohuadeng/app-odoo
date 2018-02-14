# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError
import time

class ProductSetSupplierWiz(models.TransientModel):
    _name = 'product.set.supplier.wiz'
    _description = 'Set supplier for product'

    name = fields.Many2one(
        'res.partner', 'Vendor',
        domain=[('supplier', '=', True)], ondelete='cascade', required=True,
        help="Vendor of this product")
    min_qty = fields.Float(
        'Minimal Quantity', default=0.0, required=True,
        help="The minimal quantity to purchase from this vendor, expressed in the vendor Product Unit of Measure if not any, in the default unit of measure of the product otherwise.")
    price = fields.Float(
        'Price', default=0.0, digits=dp.get_precision('Product Price'),
        required=True, help="The price to purchase a product")
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one(
        'res.currency', 'Currency',
        default=lambda self: self.env.user.company_id.currency_id.id,
        required=True)
    date_start = fields.Date('Start Date', help="Start date for this vendor price")
    date_end = fields.Date('End Date', help="End date for this vendor price")
    delay = fields.Integer(
        'Delivery Lead Time', default=1, required=True,
        help="Lead time in days between the confirmation of the purchase order and the receipt of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.")

    # 通过过滤得到要设置的补货单
    p_ids = fields.Many2many('procurement.order', string='Procurement to set', readonly=True)
    # 设置完后是否直接显示po
    view_po = fields.Boolean('Show relate RFQ after set supplier', default=True)

    # 默认值
    @api.model
    def default_get(self, fields):
        res = super(ProductSetSupplierWiz, self).default_get(fields)
        res['create_uid'] = self.env.user.id
        if not res.get('min_qty'):
            res['min_qty'] = 1
        if not res.get('date_start'):
            res['date_start'] = datetime.now().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        if not res.get('date_end'):
            res['date_end'] = (datetime.now() + timedelta(days=1)).strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        procs_ids = self.env.context.get('active_ids')
        procs = self.env['procurement.order'].browse(procs_ids).filtered(lambda x: x.rule_id.action == 'buy' and x.state == 'exception')
        p_ids = procs.ids
        res['p_ids'] = p_ids
        if len(p_ids) < 1:
            raise UserError(_("Please select valid procurement orders. Only the 'status=Exception' and 'Buy in Inventory Routes' product can be set!"))
        # 请选择有效的补货单。只有需要采购的异常补货单才可进行设置！
        return res

    # 为选定的产品设定供应商，只处理系统没处理的
    @api.multi
    def set_supplier(self):
        self.ensure_one()
        procs_ids = self.env.context.get('active_ids')
        procs = self.env['procurement.order'].browse(procs_ids).filtered(lambda x: x.rule_id.action == 'buy' and x.state == 'exception')
        t_ids = procs.mapped('product_id.product_tmpl_id').ids
        # 去重复
        t_ids = list(set(t_ids))
        for t in t_ids:
            self.env['product.supplierinfo'].create({
                'name': self.name.id,
                'product_tmpl_id': t,
                'min_qty': self.min_qty,
                'date_start': self.date_start,
                'date_end': self.date_end,
                'delay': self.delay,
            })
        time.sleep(1)
        procs.run()
        if self.view_po:
            time.sleep(2)
            p_names = procs.mapped('purchase_id.name')
            p_names = list(set(p_names))
            domain = [["name", "in", p_names]]
            context = {
                'search_default_name': p_names[0],
            }
            action = self.env.ref('purchase.purchase_rfq').read()[0]
            if len(p_names) == 1:
                action.update({
                    'context': context,
                })
            elif len(p_names) > 1:
                action.update({
                    'domain': domain,
                })
            return action
