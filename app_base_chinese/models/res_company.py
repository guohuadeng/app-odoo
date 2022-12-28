# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    def _adjust_wh_cn_name(self):
        companys = self.env['res.company'].with_context(active_test=False, lang='zh_CN').search([])
        for rec in companys:
            # 修正区位名称
            ids = self.env['stock.location'].with_context(active_test=False).search(
                [('name', 'like', ': Transit Location'), ('company_id', '=', rec.id)])
            ids.write({'name': '%s: 中转区位' % rec.name})
            ids = self.env['stock.location'].with_context(active_test=False).search(
                [('name', 'like', ': Scrap'), ('company_id', '=', rec.id)])
            ids.write({'name': '%s: 报废区位' % rec.name})
            ids = self.env['stock.location'].with_context(active_test=False).search(
                [('name', 'like', ': Inventory adjustment'), ('company_id', '=', rec.id)])
            ids.write({'name': '%s: 盘点区位' % rec.name})
            # 注意，原生没有在生产中使用 _
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', 'like', ': Production'), ('company_id', '=', rec.id)])
            ids.write({'name': '%s: 生产区位' % rec.name})
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', 'like', ': Subcontracting Location'), ('company_id', '=', rec.id)])
            ids.write({'name': '%s: 委外区位' % rec.name})
