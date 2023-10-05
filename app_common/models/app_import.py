# -*- coding: utf-8 -*-

import base64
import io
import csv
import os.path

from odoo import api, fields, models, modules, tools, SUPERUSER_ID, _
from odoo.tools import pycompat
from odoo.tests import common
ADMIN_USER_ID = common.ADMIN_USER_ID

def app_quick_import(cr, content_path, sep=None):
    if not sep:
        sep = '/'
    dir_split = content_path.split(sep)
    module_name = dir_split[0]
    file_name = dir_split[2]
    file_path, file_type = os.path.splitext(content_path)
    model_name = file_name.replace(file_type, '')
    file_path = modules.get_module_resource(module_name, dir_split[1], file_name)
    content = open(file_path, 'rb').read()
    uid = SUPERUSER_ID
    if model_name == 'mail.channel':
        # todo: 创建mail.channel时，如果用root用户会报错
        uid = 2
    env = api.Environment(cr, uid, {})
    if file_type == '.csv':
        file_type = 'text/csv'
    elif file_type in ['.xls', '.xlsx']:
        file_type = 'application/vnd.ms-excel'
    import_wizard = env['base_import.import'].create({
        'res_model': model_name,
        'file_name': file_name,
        'file_type': file_type,
        'file': content,
    })
    if file_type == 'text/csv':
        preview = import_wizard.parse_preview({
            'separator': ',',
            'has_headers': True,
            'quoting': '"',
        })
    elif file_type == 'application/vnd.ms-excel':
        preview = import_wizard.parse_preview({
            'has_headers': True,
        })
    result = import_wizard.execute_import(
        preview["headers"],
        preview["headers"],
        preview["options"]
    )


