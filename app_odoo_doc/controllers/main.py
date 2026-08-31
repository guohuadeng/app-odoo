# -*- coding: utf-8 -*-

from odoo import http, modules
from odoo.http import request


class DocumentationController(http.Controller):

    @http.route([
        '/documentation/<string:version>/<path:file_name>',
    ], methods=['GET'], type='http', auth='public')
    def redirect_to_doc(self, file_name, version='19.0'):
        # todo: 当前不处理多语言，因为会将 path 和 lang 混。后续 取所有语言，然后再判断
        module_path = modules.get_module_path('app_odoo_doc', display_warning=False)

        if module_path:
            base_url_doc = request.httprequest.full_path
            if base_url_doc.endswith('?'):
                base_url_doc = base_url_doc[:-1]
            # 当前只处理 英文
            user_lang = False
            if request.session.uid:
                user_lang = request.env['res.users'].sudo().browse(request.session.uid).partner_id.lang
            if user_lang and file_name.startswith(user_lang):
                base_url_doc = base_url_doc.replace(('/%s' % user_lang), '')
                return request.redirect(base_url_doc, 303)
        #     todo: 当前直接303转资源
        return request.redirect('/app_odoo_doc/static%s' % base_url_doc, 303)
