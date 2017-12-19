# -*- coding: utf-8 -*-

# Created on 2017-11-05
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


class ProductInternalType(models.Model):
    _name = "product.internal.type"

    name = fields.Char('Display Name', default='Normal', translate=True)
    description = fields.Char('Description')
    ref = fields.Char('Unique Code', required=True)

    link_sequence = fields.Many2one(
        'ir.sequence', 'Link Sequence',
        auto_join=True, required=True, domain="[('code', '=', 'product.product')]")
    sequence_prefix = fields.Char(u'Sequence Prefix', related='link_sequence.prefix', readonly=True, store=False)
    # 各种默认值，填则自动录入，不填则不管
    type = fields.Selection([
        ('consu', _('Consumable')),
        ('service', _('Service')),
        ('product', _('Stockable Product'))], string='Product Type',
        help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
             'A consumable product, on the other hand, is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.\n'
             'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
             'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')

    rental = fields.Boolean('Can be Rent')
    sale_ok = fields.Boolean(
        'Can be Sold', default=True,
        help="Specify if the product can be selected in a sales order line.")
    purchase_ok = fields.Boolean('Can be Purchased', default=True)
    
    # 使用目录的默认路线来处理，暂时不用内部类型路线
    route_ids = fields.Many2many('stock.location.route', string='Routes',
        domain=[('product_selectable', '=', True)],
        help="Depending on the modules installed, this will allow you to define the route of the product: whether it will be bought, manufactured, MTO/MTS,...")

    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.user.company_id.id, index=1)

    _sql_constraints = [
        ('uniq_ref',
         'unique(ref)',
         'The reference must be unique'),
    ]