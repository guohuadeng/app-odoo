# -*- coding: utf-8 -*-

import logging
import lxml.html
from odoo import api, fields, models, modules, tools, _

_logger = logging.getLogger(__name__)


class Module(models.Model):
    _inherit = "ir.module.module"

    description_html_cn = fields.Html('Description HTML CN', compute='_get_desc_cn')

    @api.depends('name', 'description')
    def _get_desc_cn(self):
        for module in self:
            module_path = modules.get_module_path(module.name, display_warning=False)  # avoid to log warning for fake community module
            if module_path:
                path = modules.check_resource_path(module_path, 'static/description/index_cn.html')
            else:
                module.description_html_cn = False
            if module_path and path:
                # 注意： b 不能在 mode中才能使用 utf-8
                with tools.file_open(path, 'r') as desc_file:
                    doc = desc_file.read()
                    html = lxml.html.document_fromstring(doc)
                    for element, attribute, link, pos in html.iterlinks():
                        if element.get('src') and not '//' in element.get('src') and not 'static/' in element.get('src'):
                            element.set('src', "/%s/static/description/%s" % (module.name, element.get('src')))
                    module.description_html_cn = tools.html_sanitize(lxml.html.tostring(html))
            else:
                module.description_html_cn = False
