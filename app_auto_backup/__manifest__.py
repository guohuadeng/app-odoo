# -*- coding: utf-8 -*-
#    'author': "Yenthe Van Ginneken",
#    'website': "http://www.odoo.yenthevg.com",

{
    'name': "Database auto-backup,数据库自动备份",
    'version': '16.23.06.25',

    'summary': 'Automated backups, optimized from auto_backup of Yenthe Van Ginneken',

    'description': """
        The Database Auto-Backup module enables the user to make configurations for the automatic backup of the database. 
        Backups can be taken on the local system or on a remote server, through SFTP.
        You only have to specify the hostname, port, backup location and databasename (all will be pre-filled by default with correct data.
        If you want to write to an external server with SFTP you will need to provide the IP, username and password for the remote backups.
        The base of this module is taken from Odoo SA V6.1 (https://www.odoo.com/apps/modules/6.0/auto_backup/) and then upgraded and heavily expanded.
        This module is made and provided by Yenthe Van Ginneken (Oocademy).
        Automatic backup for all such configured databases can then be scheduled as follows:  
                      
        1) Go to Settings / Technical / Automation / Scheduled actions.
        2) Search the action 'Backup scheduler'.
        3) Set it active and choose how often you wish to take backups.
        4) If you want to write backups to a remote location you should fill in the SFTP details.
    """,

    'author': 'Sunpop.cn',
    'website': "http://www.sunpop.cn",
    'category': 'Administration',
    'installable': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': ['paramiko'],
    },

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/backup_view.xml',
        'data/backup_data.xml',
    ],
}
