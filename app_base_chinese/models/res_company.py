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

            # 修正高级路线的中文名称：stock.route.name 是可翻译字段，
            # 用 zh_CN 上下文写入只覆盖中文翻译，英文原名保持不变。
            route_names = {
                'Deliver in 1 step (ship)': '一步发货(出库)',
                'Deliver in 2 steps (pick + ship)': '二步出货(拣货>发货)',
                'Deliver in 3 steps (pick + pack + ship)': '三步出货(拣货>包装>发货)',
                'Receive in 1 step (stock)': '一步收货(入库)',
                'Receive in 2 steps (input + stock)': '二步收货(收货>库存)',
                'Receive in 3 steps (input + quality + stock)': '三步收货(收货>质检>入库)',
            }
            Route = self.env['stock.route'].with_context(active_test=False)
            for en_name, cn_name in route_names.items():
                # 仓库生成的高级路线名形如“广州仓: Receive in 1 step (stock)”，
                # 需按英文片段模糊检索，并保留“仓库名: ”前缀只替换路线部分
                routes = Route.with_context(lang='en_US').search([('name', 'ilike', en_name)])
                for route in routes:
                    zh_name = route.with_context(lang='zh_CN').name or ''
                    # 保留“仓库名: ”前缀，后段统一重建为目标中文名（幂等，重复执行不再变化）
                    prefix = zh_name.rsplit(': ', 1)[0] if ': ' in zh_name else ''
                    new_name = '%s: %s' % (prefix, cn_name) if prefix else cn_name
                    if new_name != zh_name:
                        route.with_context(lang='zh_CN').write({'name': new_name})

            ids = self.env['stock.location'].with_context(active_test=False).search([
                ('company_id', '=', rec.id)
            ])
            ids._compute_complete_name()
