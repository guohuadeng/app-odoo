# -*- coding: utf-8 -*-
#    'author': "Yenthe Van Ginneken",
#    'website': "http://www.odoo.yenthevg.com",
#    'author': "guohuadeng@hotmail.com",
#    'website': "https://www.odooai.cn",

{
    'name': "数据库自动备份,Database Auto Backup and Download",
    'version': '20.0.26.09.20',

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
    10. Support Odoo 20,19,18,17,16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
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
    # paramiko 只服务于「可选」的远程 SFTP 备份功能（sftp_write 默认关闭），
    # 本地 pg_dump 备份与下载不依赖它，因此不再作为 manifest 级 external_dependencies
    # 硬门槛声明——v20 的 ir_module.check_external_dependencies()（addons/base/models/
    # ir_module.py:349）在依赖缺失时直接 raise UserError 使模块不可安装，而 v18 原有的
    # models/db_backup.py 模块级 raise ImportError 在 v20 会让整库 registry 初始化失败
    # （Couldn't load module + Failed to initialize database）。
    # 现改为 models/db_backup.py 里的软导入：缺 paramiko 时模块照常装载，
    # 只有真正触发 SFTP（测试连接 / sftp_write 远程上传）才抛中文 UserError。
    # 生产部署仍需安装：pip3 install paramiko
    'external_dependencies': {},

    # always loaded
    'data': [
        'security/user_groups.xml',
        'views/backup_view.xml',
        'data/backup_data.xml',
        'views/db_backup_details.xml',
        # v20：权限文件统一为 security/ir.access.csv，且必须放在 data 末尾
        # （v18 的旧权限 CSV 已废弃，见 base/models/ir_access.py:66）
        'security/ir.access.csv',
    ],
    'post_init_hook': 'post_init_hook',
}
