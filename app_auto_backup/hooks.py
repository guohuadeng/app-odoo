# -*- coding: utf-8 -*-


def post_init_hook(env):
    db_name = env.cr.dbname
    existing = env['db.backup'].sudo().search([('name', '=', db_name)], limit=1)
    if existing:
        return
    env['db.backup'].sudo().create({
        'host': 'localhost',
        'port': '8069',
        'name': db_name,
        'folder': '/usr/lib/python3/dist-packages/odoo/backups',
        'backup_type': 'zip',
        'days_to_keep': 30,
    })
