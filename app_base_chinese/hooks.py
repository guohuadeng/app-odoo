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
    try:
        cr.execute("UPDATE product_product "
                   "SET default_code = '!!PR!!' || id "
                   "WHERE default_code IS NULL OR default_code = 'New';")
        pass
    except Exception as e:
        raise Warning(e)
