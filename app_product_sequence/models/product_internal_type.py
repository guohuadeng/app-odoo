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

    name = fields.Char('Display Name',default='Normal')
    description = fields.Char('Description')
    # 因为default_code有odoo的处理方式，影响面大，故会将其另存到 default_code_stored
    link_sequence = fields.Many2one(
        'ir.sequence', 'Link Sequence',
        auto_join=True, required=True, domain="[('code', '=', 'product.product')]")
    sequence_prefix = fields.Char(u'Sequence Prefix', related='link_sequence.prefix', readonly=True, store=False)

    # _sql_constraints = [
    #     ('uniq_link_sequence',
    #      'unique(link_sequence)',
    #      'The Link Sequence must be unique'),
    # ]