# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request


class KsHome(Home):

    @http.route()
    def web_client(self, s_action=None, **kw):
        res = super(KsHome, self).web_client(s_action, **kw)

        if kw.get('debug') in ['1', 'assets', 'assets,tests']:
            config_parameter = request.env['ir.config_parameter'].sudo()
            app_debug_only_admin = config_parameter.get_param('app_debug_only_admin')
            if request.session.uid and request.env.user.browse(request.session.uid)._is_admin():
                pass
            else:
                if app_debug_only_admin:
                    return request.redirect('/web/session/logout?debug=0')
        return res



