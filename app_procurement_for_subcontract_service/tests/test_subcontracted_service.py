# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo import fields


class TestSubcontractedService(TransactionCase):
    def setUp(self):
        super(TestSubcontractedService, self).setUp()
        self.procurement_group_obj = self.env['procurement.group']
        self.obj_warehouse = self.env['stock.warehouse']

        # 1. find a supplier
        self.supplier = self.env.ref('base.res_partner_1')

        # 2. create a service product unconfigured
        values = {'name': 'Service Subcontracted',
                  'type': 'service',
                  'seller_ids': [(0, 0, {
                      'name': self.supplier.id,
                      'price': 100.0,
                  })]
                  }
        self.pdt_service = self.env['product.product'].create(values)
        # 3. create a test warehouse
        self.test_wh = self.obj_warehouse.create({
            'name': 'Test WH',
            'code': 'T',
        })
        # 4. find a customer
        self.customer = self.env['res.partner'].search(
            [('customer', '=', True)],
            limit=1
        )

    def test_wh_procurement_rule(self):
        """Tests if the procurement rule for subcontracting services is
        assigned properly to the warehouse."""
        wh = self.test_wh
        self.assertNotEqual(wh.subcontracting_service_proc_rule_id, False,
                            'Subcontracting Service Rule not assigned to the '
                            'Warehouse.')
        picking_wh = wh.subcontracting_service_proc_rule_id.\
            picking_type_id.warehouse_id
        self.assertEqual(picking_wh, wh, 'Rule wrongly configured.')

    def test_subcontracted_service_procurement(self):
        """Test if the subcontracting service procurement rule is correctly
        assigned when creating a procurement for a subcontracted service
        product."""
        values = {
            'warehouse_id': self.test_wh,
            'company_id': self.test_wh.company_id,
            'date_planned': fields.Date.today(),
            'group_id': self.test_wh.
            subcontracting_service_proc_rule_id.group_id,
        }
        self.pdt_service.property_subcontracted_service = True
        self.procurement_group_obj.run(
            self.pdt_service, 1,
            self.pdt_service.uom_id,
            self.test_wh.lot_stock_id, 'test', 'test', values)
        po_line = self.env['purchase.order.line'].search(
            [('product_id', '=', self.pdt_service.id)], limit=1)
        self.assertEqual(len(po_line), 1)
        self.assertEqual(po_line.product_qty, 1)
        self.assertEqual(po_line.product_uom, self.pdt_service.uom_id)
        self.assertEqual(po_line.order_id.group_id,
                         self.test_wh.
                         subcontracting_service_proc_rule_id.group_id)
        self.assertEqual(po_line.company_id, self.test_wh.company_id)
