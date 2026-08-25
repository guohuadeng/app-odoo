# -*- coding: utf-8 -*-
#    'author': "Yenthe Van Ginneken",
#    'website': "http://www.odoo.yenthevg.com",
#    'author': "guohuadeng@hotmail.com",
#    'website': "https://www.odooai.cn",

{
    'name': "数据库自动备份,Database Auto Backup and Download",
    'version': '18.0.26.08.25',

    'summary': "Odoo数据库自动备份、远程SFTP备份、一键手动备份、备份文件下载管理。Automated database backup with SFTP remote backup, manual one-click backup and easy download.",

    'description': """
    1. Easy schedule database backup via cron job.
    2. Set remote SFTP backup with encrypted SSH tunnel.
    3. Manual backup database in one click.
    4. Easy download backup file or remove file for System user.
    5. Test SFTP connection in one click.
    6. Auto e-mail notification on backup failure.
    7. Specify how long local and remote backups should be kept.
    8. Based on Yenthe Van Ginneken's auto_backup, upgraded and expanded.
    9. Multi-language Support. Multi-Company Support.
    10. Support Odoo 19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    11. Full Open Source.

    1. 通过定时任务轻松设置数据库自动备份
    2. 支持远程SFTP加密SSH隧道备份
    3. 一键手动备份数据库
    4. 系统用户可直接下载或删除备份文件
    5. 一键测试SFTP连接
    6. 备份失败自动邮件通知
    7. 可设置本地和远程备份保留天数
    8. 基于Yenthe Van Ginneken的auto_backup升级扩展
    9. 多语言支持，多公司支持
    10. Odoo 19,18,17,16,15,14,13,12, 企业版，社区版，在线SaaS.sh版，等全版本支持
    11. 代码完全开源
    """,

    'author': 'odooai.cn',
    'website': "http://www.odooai.cn",
    'category': 'Extra tools',
    'installable': True,
    'license': 'LGPL-3',
    'price': 38.00,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'app_odoo_customize'
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
        'views/db_backup_details.xml',
    ],
    'post_init_hook': 'post_init_hook',
}
