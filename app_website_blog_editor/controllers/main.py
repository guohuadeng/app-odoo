# -*- coding: utf-8 -*-

import re
import werkzeug
from odoo import http, fields, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog


class WebsiteBlog(WebsiteBlog):

    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False, page=False, search=None):
        blogs = blogs.sorted(key='sequence')
        res = super(WebsiteBlog, self)._prepare_blog_values(blogs, blog, date_begin, date_end, tags, state, page, search)
        return res
        
