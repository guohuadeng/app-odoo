# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

from odoo import api, SUPERUSER_ID, _

def pre_init_hook(cr):
    pass

def post_init_hook(cr, registry):
    try:
        env = api.Environment(cr, SUPERUSER_ID, {})
        g = env.ref('app_stock_picking_type_group.g_sale1', raise_if_not_found=False).id
        cr.execute("UPDATE stock_picking_type SET picking_type_group_id = %s WHERE code='outgoing';" % g)

        env = api.Environment(cr, SUPERUSER_ID, {})
        g = env.ref('app_stock_picking_type_group.g_purchase1', raise_if_not_found=False).id
        cr.execute("UPDATE stock_picking_type SET picking_type_group_id = %s WHERE code='incoming';" % g)

        env = api.Environment(cr, SUPERUSER_ID, {})
        g = env.ref('app_stock_picking_type_group.g_mrp1', raise_if_not_found=False).id
        cr.execute("UPDATE stock_picking_type SET picking_type_group_id = %s WHERE code='mrp_operation';" % g)

        env = api.Environment(cr, SUPERUSER_ID, {})
        g = env.ref('app_stock_picking_type_group.g_stock1', raise_if_not_found=False).id
        cr.execute("UPDATE stock_picking_type SET picking_type_group_id = %s WHERE code='internal';" % g)
        pass
    except Exception as e:
        raise Warning(e)
