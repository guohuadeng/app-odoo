# -*- coding: utf-8 -*-

import re
import werkzeug
from odoo import http, fields, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog


class WebsiteBlog(WebsiteBlog):

    @http.route([
        '/blog',
        '/blog/page/<int:page>',
        '/blog/tag/<string:tag>',
        '/blog/tag/<string:tag>/page/<int:page>',
        '''/blog/<model("blog.blog"):blog>''',
        '''/blog/<model("blog.blog"):blog>/page/<int:page>''',
        '''/blog/<model("blog.blog"):blog>/tag/<string:tag>''',
        '''/blog/<model("blog.blog"):blog>/tag/<string:tag>/page/<int:page>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog(self, blog=None, tag=None, page=1, search=None, **opt):
        Blog = request.env['blog.blog']

        # TODO adapt in master. This is a fix for templates wrongly using the
        # 'blog_url' QueryURL which is defined below. Indeed, in the case where
        # we are rendering a blog page where no specific blog is selected we
        # define(d) that as `QueryURL('/blog', ['tag'], ...)` but then some
        # parts of the template used it like this: `blog_url(blog=XXX)` thus
        # generating an URL like "/blog?blog=blog.blog(2,)". Adding "blog" to
        # the list of params would not be right as would create "/blog/blog/2"
        # which is still wrong as we want "/blog/2". And of course the "/blog"
        # prefix in the QueryURL definition is needed in case we only specify a
        # tag via `blog_url(tab=X)` (we expect /blog/tag/X). Patching QueryURL
        # or making blog_url a custom function instead of a QueryURL instance
        # could be a solution but it was judged not stable enough. We'll do that
        # in master. Here we only support "/blog?blog=blog.blog(2,)" URLs.
        if isinstance(blog, str):
            blog = Blog.browse(int(re.search(r'\d+', blog)[0]))
            if not blog.exists():
                raise werkzeug.exceptions.NotFound()

        blogs = tools.lazy(lambda: Blog.search(request.website.website_domain(), order="sequence asc, name asc"))

        if not blog and len(blogs) == 1:
            url = QueryURL('/blog/%s' % slug(blogs[0]), search=search, **opt)()
            return request.redirect(url, code=302)

        date_begin, date_end, state = opt.get('date_begin'), opt.get('date_end'), opt.get('state')

        if tag and request.httprequest.method == 'GET':
            # redirect get tag-1,tag-2 -> get tag-1
            tags = tag.split(',')
            if len(tags) > 1:
                url = QueryURL('' if blog else '/blog', ['blog', 'tag'], blog=blog, tag=tags[0], date_begin=date_begin, date_end=date_end, search=search)()
                return request.redirect(url, code=302)

        values = self._prepare_blog_values(blogs=blogs, blog=blog, date_begin=date_begin, date_end=date_end, tags=tag, state=state, page=page, search=search)

        # in case of a redirection need by `_prepare_blog_values` we follow it
        if isinstance(values, werkzeug.wrappers.Response):
            return values

        if blog:
            values['main_object'] = blog
            values['blog_url'] = QueryURL('', ['blog', 'tag'], blog=blog, tag=tag, date_begin=date_begin, date_end=date_end, search=search)
        else:
            values['blog_url'] = QueryURL('/blog', ['tag'], date_begin=date_begin, date_end=date_end, search=search)

        return request.render("website_blog.blog_post_short", values)
