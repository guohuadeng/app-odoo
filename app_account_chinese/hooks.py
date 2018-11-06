# -*- coding: utf-8 -*-

# Created on 2017-11-22
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

from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    """
    数据初始化，只在安装时执行，更新时不执行
    """
    pass


def post_init_hook(cr, registry):
    """
    数据初始化，只在安装后执行，更新时不执行
    此处不执行，只是记录，该数据已处理完成
    """
    cr.execute("UPDATE account_account set group_id = "
               "(select id from account_group where account_group.code_prefix=trim(substring(account_account.code from 1 for 1)) limit 1);")

    cr.execute("UPDATE account_tax set amount=16, name='增值税16%销项税'"
               " where name like '增值税17%销项税%' and amount_type='percent';")

    cr.execute("UPDATE account_tax set amount=16, name='增值税16%进项税'"
               " where name like '增值税17%进项税%' and amount_type='percent';")

    pass

