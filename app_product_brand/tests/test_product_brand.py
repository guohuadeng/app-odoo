# Copyright (c) 2018 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class TestProductBrand(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.product = self.env.ref('product.product_product_4')
        self.supplier = self.ref('base.res_partner_2')
        self.product_brand_obj = self.env['product.brand']
        self.product_brand = self.product_brand_obj.create(
            {'name': 'Test Brand',
             'description': 'Test brand description',
             'partner_id': self.supplier
             })

    def test_products_count(self):
        self.assertEqual(self.product_brand.products_count, 0,
                         'Error product count does not match')
        self.product.product_brand_id = self.product_brand.id
        self.assertEqual(self.product_brand.products_count, 1,
                         'Error product count does not match')
