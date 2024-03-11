# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request


class AppHome(Home):

    @http.route()
    def web_client(self, s_action=None, **kw):
        res = super(AppHome, self).web_client(s_action, **kw)
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user') \
                and kw.get('debug', False):
            app_debug_only_admin = 1
            if request.session.uid and request.env.user.browse(request.session.uid)._is_admin():
                pass
            else:
                if app_debug_only_admin:
                    return request.redirect('/web/session/logout?debug=0')
        return res
