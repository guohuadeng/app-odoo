# -*- coding: utf-8 -*-

import logging
import re
import werkzeug
from odoo import http, fields, tools
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog

_logger = logging.getLogger(__name__)


class WebsiteBlog(WebsiteBlog):

    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False, page=False, search=None, **post):
        blogs = blogs.sorted(key='sequence')
        # 清洗日期参数：URL 中的 + 号可能未被正确解码为空格，导致日期格式解析失败
        # 例: '2020-06-01+00:00:00' → '2020-06-01 00:00:00'
        if isinstance(date_begin, str):
            date_begin = date_begin.replace('+', ' ')
            try:
                date_begin = fields.Datetime.from_string(date_begin)
            except (ValueError, TypeError):
                _logger.warning('无法解析博客日期参数 date_begin: %s，已忽略', date_begin)
                date_begin = False
        if isinstance(date_end, str):
            date_end = date_end.replace('+', ' ')
            try:
                date_end = fields.Datetime.from_string(date_end)
            except (ValueError, TypeError):
                _logger.warning('无法解析博客日期参数 date_end: %s，已忽略', date_end)
                date_end = False
        res = super(WebsiteBlog, self)._prepare_blog_values(blogs, blog, date_begin, date_end, tags, state, page, search, **post)
        return res

