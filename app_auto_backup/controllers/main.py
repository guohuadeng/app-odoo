# -*- coding: utf-8 -*-

import logging
import os

from odoo import http, _
from odoo.http import request, content_disposition
from odoo.exceptions import AccessError, UserError

_logger = logging.getLogger(__name__)


class AppAutoBackup(http.Controller):
    
    @http.route("/dbbackup/download/<path:file_path>", type="http", auth="user")
    def download_backupfile(self, file_path, **kw):
        _logger.warning('download_backupfile: %s', file_path)
        if not self.env.user.has_group('base.group_system'):
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
