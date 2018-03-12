# -*- coding: utf-8 -*-

# Created on 2018-03-12
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:

from openerp import api, fields, models, _

class PackOperation(models.Model):
    _inherit = "stock.pack.operation"

    @api.multi
    def _compute_product_supplier_code(self):
        product_supplierinfo_obj = self.env['product.supplierinfo']
        for line in self:
            partner = line.picking_id.partner_id
            product = line.product_id
            if product and partner:
                supplier_info = product_supplierinfo_obj.search([
                    '|', ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('product_id', '=', product.id),
                    ('name', '=', partner.id)], limit=1)
                if supplier_info:
                    code = supplier_info.product_code or ''
                    line.product_supplier_code = code
        return True

    product_supplier_code = fields.Char(string='Product Supplier Code',
                                        compute=_compute_product_supplier_code)
