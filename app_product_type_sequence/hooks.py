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

def pre_init_hook(cr):
    """
    Updates existing codes matching the default 'New' or
    empty. Primarily this ensures installation does not
    fail for demo data.
    :param cr: database cursor
    :return: void
    """
    cr.execute("UPDATE product_product "
               "SET default_code = '!!DP!!' || id "
               "WHERE default_code IS NULL OR default_code = 'New';")

    cr.execute("UPDATE product_template "
               "Set default_code = "
               "(select default_code from product_product "
               "where product_product.product_tmpl_id = product_template.id limit 1)"
               "WHERE default_code IS NULL OR default_code = 'New';")
