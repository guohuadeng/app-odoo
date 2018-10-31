# -*- coding: utf-8 -*-

# Created on 2017-11-28
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

from odoo import api, fields, models, exceptions, _

class ProductCategory(models.Model):
    _inherit = 'product.category'
    _order = 'sequence, ref'

    ref = fields.Char(u'唯一编码', index=True)
    sequence = fields.Integer(u'排序', help="Determine the display order")

    # 增加目录编号唯一检查
    # _sql_constraints = [
    #     ('uniq_ref',
    #      'unique(ref)',
    #      'The reference must be unique'),
    # ]

    # 产品目录序号器，正常全部手工录入
    @api.model
    def create(self, vals):
        if not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('product.category.seq.normal')
        if vals.get('ref'):
            vals['ref'] = vals['ref'].upper()
        return super(ProductCategory, self).create(vals)

