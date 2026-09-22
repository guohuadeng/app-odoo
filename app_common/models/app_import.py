# -*- coding: utf-8 -*-

import os.path

from odoo import SUPERUSER_ID, _
from odoo.tools import misc

def app_quick_import(env, content_path, sep=None, context={}):
    if not sep:
        sep = '/'
    dir_split = content_path.split(sep)
    file_name = dir_split[2]
    file_base, file_type = os.path.splitext(content_path)
    model_name = file_name.replace(file_type, '')
    # Odoo 17.0+ 弃用 modules.get_module_resource，改用 tools.misc.file_path
    full_path = misc.file_path(content_path)
    with open(full_path, 'rb') as f:
        content = f.read()
    uid = SUPERUSER_ID
    if model_name == 'discuss.channel':
        # todo: 创建discuss.channel时，如果用root用户会报错
        uid = 2
    if file_type == '.csv':
        file_type = 'text/csv'
    elif file_type in ['.xls', '.xlsx']:
        file_type = 'application/vnd.ms-excel'
    import_wizard = env['base_import.import'].with_context(context)
    import_wizard = import_wizard.create({
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
    else:
        preview = False
    
    if preview:
        import_wizard.execute_import(
            preview["headers"],
            preview["headers"],
            preview["options"]
        )


