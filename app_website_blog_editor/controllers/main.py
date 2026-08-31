# -*- coding: utf-8 -*-

import logging
import re
import werkzeug
from odoo import http, fields, tools
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog

_logger = logging.getLogger(__name__)


# 日期格式正则：仅匹配形如 YYYY-MM-DD 或 YYYY-MM-DD HH:MM:SS 的合法日期字符串
_DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}(\s+\d{2}:\d{2}(:\d{2})?)?$')


class WebsiteBlog(WebsiteBlog):

    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False, page=False, search=None, **post):
        blogs = blogs.sorted(key='sequence')
        # 清洗日期参数：URL 中的 + 号可能未被正确解码为空格，导致日期格式解析失败
        # 例: '2020-06-01+00:00:00' → '2020-06-01 00:00:00'
        # 同时过滤掉非日期字符串的参数（如记录ID '427037174'）
        if isinstance(date_begin, str):
            date_begin = date_begin.replace('+', ' ')
            if _DATE_RE.match(date_begin):
                try:
                    date_begin = fields.Datetime.from_string(date_begin)
                except (ValueError, TypeError):
                    _logger.debug('无法解析博客日期参数 date_begin: %s，已忽略', date_begin)
                    date_begin = False
            else:
                date_begin = False
        if isinstance(date_end, str):
            date_end = date_end.replace('+', ' ')
            if _DATE_RE.match(date_end):
                try:
                    date_end = fields.Datetime.from_string(date_end)
                except (ValueError, TypeError):
                    _logger.debug('无法解析博客日期参数 date_end: %s，已忽略', date_end)
                    date_end = False
            else:
                date_end = False
        res = super(WebsiteBlog, self)._prepare_blog_values(blogs, blog, date_begin, date_end, tags, state, page, search, **post)
        return res

