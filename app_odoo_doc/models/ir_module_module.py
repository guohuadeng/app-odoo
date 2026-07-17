# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, tools, _
from odoo.exceptions import UserError
import odoo.release
from odoo.tools import get_lang
from odoo.addons.app_common.models.app_import import app_quick_import


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
        url_site = ICP.get_param("app_doc_root_url", '')
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
        try:
            app_quick_import(self.env, 'app_odoo_doc/data/ir.module.module.csv')
        except Exception as e:
            pass

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
