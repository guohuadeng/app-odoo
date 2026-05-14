# -*- coding: utf-8 -*-

from odoo import api, SUPERUSER_ID, _
from odoo.exceptions import UserError


def pre_init_hook(cr):
    """
    安装前检查：必须已安装并启用英文语言包 (en_US)
    """
    cr.execute("SELECT id FROM res_lang WHERE code = 'en_US' AND active = TRUE")
    if not cr.fetchone():
        raise UserError(_(
            "English language (en_US) must be enabled before installing this module.\n"
            "Please install it from Settings > Translations > Languages."
        ))


def post_init_hook(env):
    """
    数据初始化，只在安装后执行，更新时不执行
    """
    pass


def uninstall_hook(env):
    """
    数据初始化，卸载时执行
    """
    pass
