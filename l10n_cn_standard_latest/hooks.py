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

from odoo import api, SUPERUSER_ID

def pre_init_hook(env):
    """
    数据初始化，只在安装时执行，更新时不执行
    """
    pass


def post_init_hook(env):
    """
    数据初始化，只在安装后执行，更新时不执行
    中国公司，会计科目表非本模块中国企业会计科目表时，重载

    """
    ids = env['res.company'].search([('currency_id', '=', env.ref('base.CNY').id)])
    if ids:
        ids.app_set_to_odooai_cn()
    # cr.execute("UPDATE account_account_template set group_id = "
    #            "(select id from account_group where account_group.code_prefix_start=trim(substring(account_account_template.code from 1 for 1)) limit 1);")

    # for g in [
    #     env.ref('l10n_cn_standard_latest.account_group_1'),
    #     env.ref('l10n_cn_standard_latest.account_group_2'),
    #     env.ref('l10n_cn_standard_latest.account_group_3'),
    #     env.ref('l10n_cn_standard_latest.account_group_4'),
    #     env.ref('l10n_cn_standard_latest.account_group_5'),
    #     env.ref('l10n_cn_standard_latest.account_group_6'),
    # ]:
    #     res = env['account.account'].search([('code', 'like', g.code_prefix_start + '%')])
    #     if res:
    #         res.write({'group_id': g.id})
    #     env.cr.commit()
    pass

