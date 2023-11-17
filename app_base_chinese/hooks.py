# -*- coding: utf-8 -*-

# Created on 2017-11-22
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

from odoo import api, SUPERUSER_ID, _


def pre_init_hook(cr):
    """
    数据初始化，只在安装时执行，更新时不执行
    """
    # todo: 启用中文
    pass


def post_init_hook(cr, registry):
    """
    数据初始化，只在安装后执行，更新时不执行
    """
    try:
        env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
        ids = env['product.category'].sudo().with_context(lang='zh_CN').search([
            ('parent_id', '!=', False)
        ], order='parent_path')
        for rec in ids:
            rec._compute_complete_name()
        ids = env['stock.location'].sudo().with_context(lang='zh_CN').search([
            ('location_id', '!=', False),
            ('usage', '!=', 'views'),
        ], order='parent_path')
        for rec in ids:
            rec._compute_complete_name()
        # 超级用户改时区为中国
        ids = env['res.users'].sudo().with_context(lang='zh_CN').browse([1, 2])
        ids.write({'tz': "Etc/GMT-8"})
        # 公司价格改人民币
        ids = env['res.company'].sudo().search([], limit=1)
        if ids:
            ids.write({'currency_id': env.ref('base.CNY').id})
        # 价格表改人民币
        ids = env['product.pricelist'].sudo().search([], limit=1)
        if ids:
            ids.write({'currency_id': env.ref('base.CNY').id})
    except Exception as e:
        raise Warning(e)

def uninstall_hook(cr, registry):
    """
    数据初始化，卸载时执行
    """
    pass
