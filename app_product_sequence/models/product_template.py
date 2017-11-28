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

from openerp import api, fields, models, exceptions, _


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ['product.template']

    internal_type = fields.Many2one(
        'product.internal.type', 'Internal Type',
        auto_join=True, required=True)

    default_code = fields.Char(
        'Internal Reference', compute='_compute_default_code',
        inverse='_set_default_code', store=True, readonly=True,
        default='New', copy=False)
    # 因为default_code有odoo的处理方式，影响面大，故会将其另存到 default_code_stored
    default_code_stored = fields.Char('Internal Reference Stored',default='New')

    @api.model
    def create(self, vals):
        if 'attribute_line_ids' in vals:
            if len(vals['attribute_line_ids'])>0:
                raise exceptions.ValidationError(_('Please save product first before adding varients!'))
        if 'default_code' not in vals or vals['default_code'] == 'New':
            sequence = self.env['product.internal.type'].search([('id', '=', vals['internal_type'])], limit=1)
            vals['default_code'] = sequence.link_sequence.next_by_id()
        vals['default_code_stored'] = vals['default_code']
        return super(ProductTemplate, self).create(vals)

    @api.depends('product_variant_ids', 'product_variant_ids.default_code')
    def _compute_default_code(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.default_code = template.product_variant_ids.default_code
        for template in (self):
            if len(template.product_variant_ids)>1:
                template.default_code = ''

    @api.one
    def _set_default_code(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.default_code = self.default_code_stored

    @api.onchange('categ_id')
    def _onchange_cate_id(self):
        if self.categ_id and self.categ_id.internal_type:
            self.internal_type = self.categ_id.internal_type