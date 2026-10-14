# -*- coding: utf-8 -*-

import logging
import os

from odoo import http, _
# v20 断点：odoo.http 已拆成包，命名空间只导出 request/Response/Controller/route，
# content_disposition 不再从中导出（定义在 odoo/http/stream.py:34）⇒
# 原 `from odoo.http import request, content_disposition` 是模块级 ImportError，
# 会让整库 registry 初始化失败，必须改到子模块导入
from odoo.http import request
from odoo.http.stream import content_disposition
from odoo.exceptions import AccessError, UserError

_logger = logging.getLogger(__name__)


class AppAutoBackup(http.Controller):

    @http.route("/dbbackup/download/<path:file_path>", type="http", auth="user")
    def download_backupfile(self, file_path, **kw):
        _logger.warning('download_backupfile: %s', file_path)
        if not request.env.user.has_group('base.group_system'):
            raise UserError(_('File not found for user.'))
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as file:
                    file_content = file.read()
                file_name = file_path.split("/")[-1]
                headers = [
                    ('Content-Type', 'application/octet-stream'),
                    ('Content-Disposition', content_disposition(file_name)),
                ]
                return request.make_response(file_content, headers)
            except Exception as e:
                raise UserError(e)
        else:
            return 'File not found'
