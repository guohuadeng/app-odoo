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

    # auto_join只要搜索product.template，自动会join。如果经常用到 internal_type 效率会高。
    internal_type = fields.Many2one(
        'product.internal.type', 'Internal Type',
        auto_join=True, required=True)

    default_code = fields.Char(
        'Internal Reference',
        compute='_compute_default_code',
        inverse='_set_default_code',
        store=True, default=lambda self: _('New'), copy=False)
    # 因为default_code有odoo的处理方式，影响面大，故会将其另存到 default_code_stored
    default_code_stored = fields.Char('Internal Reference Stored',default='New')

    @api.model
    def create(self, vals):
        if 'attribute_line_ids' in vals:
            if len(vals['attribute_line_ids'])>0:
                raise exceptions.ValidationError(_('Please save product first before adding varients!'))

        if not (self.env.context.get('create_product_product')):
            # 当从产品模板界面建立时（如果从产品界面建立，则已经生成了编码，不需要再处理）
            if 'default_code' not in vals or vals['default_code'] == _('New'):
                sequence = self.env['product.internal.type'].search([('id', '=', vals['internal_type'])], limit=1)
                if not sequence:
                    sequence = self.env.ref('app_product_type_sequence.internal_type_mrp_product', raise_if_not_found=False)
                vals['default_code'] = sequence.link_sequence.next_by_id()
                vals['default_code_stored'] = vals['default_code']
        return super(ProductTemplate, self).create(vals)

    @api.depends('product_variant_ids', 'product_variant_ids.default_code')
    def _compute_default_code(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.default_code = template.product_variant_ids.default_code
            template.default_code_store = template.default_code
        for template in (self):
            if len(template.product_variant_ids)>1:
                template.default_code = ''

    @api.one
    def _set_default_code(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.default_code = self.default_code_stored

    # 当内部类型变化时，改变产品模板的各默认值
    @api.onchange('internal_type')
    def _onchange_internal_type(self):
        if self.internal_type:
            self.type = self.internal_type.type
            self.rental = self.internal_type.rental
            self.sale_ok = self.internal_type.sale_ok
            self.purchase_ok = self.internal_type.purchase_ok
            self.route_ids = self.internal_type.route_ids

    # 分类变动时，如果分类绑定了内部类型则联动
    @api.onchange('categ_id')
    def _onchange_cate_id(self):
        if self.categ_id and self.categ_id.internal_type:
            self.internal_type = self.categ_id.internal_type