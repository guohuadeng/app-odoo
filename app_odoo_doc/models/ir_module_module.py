# -*- coding: utf-8 -*-

import csv
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.release
from odoo.tools import get_lang, file_path

_logger = logging.getLogger(__name__)


class IrModule(models.Model):
    _inherit = 'ir.module.module'

    base_url_doc = fields.Char(string='Doc Url', help="Help doc url router for current app. you can use http prefix or not")

    def module_go_doc(self):
        # 不用 base_url 的
        # 点击后新开窗口访问 help，无设置就 raise 说无
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        self.ensure_one()
        url = self.base_url_doc
        # app_doc_root_url = self.env['ir.config_parameter'].sudo().get_param('app_doc_root_url')
        # if url and app_doc_root_url and not url.startswith(('//', 'http://', 'https://')):
        #     url = '%s/%s' % (app_doc_root_url, url[1:] if url[0] == '/' else url)
        if not url:
            url = '/documentation/%s' % odoo.release.serie
            # return self.action_error_notify()
        # 处理语言
        lang = self.env.user.lang or get_lang(self.env).code
        if lang != 'en_US' and url.find('lang') == -1:
            url = url.replace(odoo.release.serie, '%s/%s' % (odoo.release.serie, lang))
        
        # 增加到指定网站的处理
        ICP = self.env['ir.config_parameter'].sudo()
        url_site = ICP.get_str("app_doc_root_url", '')
        if url_site and url and not url.startswith(('//', 'http://', 'https://')):
            url = '%s/%s' % (url_site, url[1:] if url[0] == '/' else url)

        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': '_new',
        }

    @api.model
    def action_xml_go_doc(self, xml_id=None):
        if not xml_id:
            mod_name = 'base'
        else:
            mod_name = xml_id.split('.')[0]
        mod = self.search([('name', '=', mod_name)], limit=1)
        if mod:
            return mod.module_go_doc()
        else:
            raise UserError(_('Module Not Found: %s' % mod_name))

    @api.model
    def app_quick_import_data(self):
        """按 xmlid 预置各应用的文档地址 data/ir.module.module.csv。

        v18 走 app_common.app_quick_import（底层是 base_import.import 的 Binary 字段 file），
        v20 起 Binary 字段拒收裸 bytes（odoo/orm/fields_binary.py:112
        “<field>: use BinaryValue instead of bytes”），而 app_common 属共享池、不在本模块可改范围，
        故这里改为直接按 xmlid 写库：缺失的 xml_id 跳过并记日志，
        避免「静默新建重复记录」（plan §六）。
        """
        try:
            with open(file_path('app_odoo_doc/data/ir.module.module.csv'), encoding='utf-8') as csv_file:
                count, skipped = 0, []
                for row in csv.DictReader(csv_file):
                    xml_id = (row.get('id') or '').strip()
                    base_url_doc = (row.get('base_url_doc') or '').strip()
                    if not xml_id or not base_url_doc:
                        continue
                    module = self.env.ref(xml_id, raise_if_not_found=False)
                    if not module or module._name != 'ir.module.module':
                        skipped.append(xml_id)
                        continue
                    module.sudo().write({'base_url_doc': base_url_doc})
                    count += 1
            if skipped:
                _logger.warning('app_odoo_doc skip missing xml_id in data/ir.module.module.csv: %s' % skipped)
            _logger.info('app_odoo_doc preset base_url_doc for %s module(s)' % count)
        except Exception as e:
            # 预置失败不阻断安装，仅记录日志便于排查
            _logger.warning('app_odoo_doc quick import data/ir.module.module.csv failed: %s' % str(e))

    @api.model
    def action_error_notify(self):
        message = _("There is currently no help document available for the current topic.")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'target': 'new',
            'params': {
                'message': message,
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }
