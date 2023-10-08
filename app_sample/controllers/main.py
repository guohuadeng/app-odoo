# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class appCustomerPortal(CustomerPortal):
    
    # Controler sample
    @http.route('/my/webclient/locale/<string:lang>', type='http', auth="none")
    def index(self, **kw):
        return "Hello, world"
        
    @http.route('/default/default/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('default.listing', {
            'root': '/default/default',
            'objects': http.request.env['default.default'].search([]),
        })
    
    @http.route('/default/default/objects/<model("default.default"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('default.object', {
            'object': obj
        })
