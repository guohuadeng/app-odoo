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

import logging
_logger = logging.getLogger(__name__)

def pre_init_hook(env):
    """
    数据初始化，只在安装时执行，更新时不执行
    """
    env['res.lang']._activate_lang('zh_CN')


def post_init_hook(env):
    """
    数据初始化，只在安装后执行，更新时不执行
    """
    try:
        ids = env['product.category'].sudo().with_context(lang='zh_CN', active_test=False).search([
            ('parent_id', '!=', False)
        ], order='parent_path')
        for rec in ids:
            rec._compute_complete_name()
        ids = env['stock.location'].sudo().with_context(lang='zh_CN', active_test=False).search([
            ('location_id', '!=', False),
            ('usage', '!=', 'views'),
        ], order='parent_path')
        for rec in ids:
            rec._compute_complete_name()
        # 超级用户及模板用户改时区为中国
        ids = env['res.users'].sudo().with_context(lang='zh_CN', active_test=False).browse([1, 2, 3, 4, 5])
        # rec_extra = env.ref('base.template_portal_user_id')
        # if rec_extra:
        #     ids += rec_extra
        ids.write({
            'tz': "Etc/GMT-8",
            'lang': "zh_CN",
        })
        # 公司价格改人民币
        ids = env['res.company'].sudo().with_context(active_test=False).search([], limit=1)
        if ids:
            try:
                ids.write({'currency_id': env.ref('base.CNY').id})
            except Exception as e:
                _logger.error('cn: company write currency_id error.')
        # 价格表改人民币
        ids = env['product.pricelist'].sudo().with_context(active_test=False).search([], limit=1)
        if ids:
            try:
                ids.write({'currency_id': env.ref('base.CNY').id})
            except Exception as e:
                _logger.error('cn: pricelist write currency_id error.')
    except Exception as e:
        raise Warning(e)

def uninstall_hook(env):
    """
    数据初始化，卸载时执行
    """
    pass
