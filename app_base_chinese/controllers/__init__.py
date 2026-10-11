# -*- coding: utf-8 -*-

# v20：本模块原 controllers/database.py 覆写 Database._render_template 做中文数据库管理器，
# v20 已把该渲染改为 web/controllers/database.py:90 的模块级函数（class Database 里只剩路由方法），
# _inherit 覆写不再生效；要恢复需猴子补丁或改走 v20 新 DB manager，属产品决策，先移除。
# 资源文件 static/src/public/database_manager.create_form.qweb.html 暂留（已无引用）。
