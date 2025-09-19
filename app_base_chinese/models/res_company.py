# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    def _adjust_wh_cn_name(self):
        companys = self.env['res.company'].with_context(active_test=False).search([('partner_id.lang', '=', 'zh_CN')])
        for rec in companys:
            # 修正区位名称，注意在新版中已非 translate 了
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Quality Control'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '质检区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Packing Zone'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '打包区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Transit Location'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '仓库间中转区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Scrap'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '报废区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Production'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '生产区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Pre-Production'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '生产领料区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Post-Production'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '成品报工区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', ': Subcontracting Location'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.with_context(lang='zh_CN').write({'name': '委外区'})
            
            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('name', '=', 'Inventory adjustment'), ('company_id', '=', rec.id)
            ])
            if ids:
                ids.write({'name': '盘点区'})

            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('company_id', '=', rec.id)
            ])
            ids._compute_complete_name()
