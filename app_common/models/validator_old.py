# -*- coding: utf-8 -*-

from odoo import tools, _
from odoo.modules.module import get_resource_path
from odoo.tools import view_validation
from odoo.tools.view_validation import validate, _validators
from lxml import etree
import logging


_logger = logging.getLogger(__name__)

_relaxng_cache = view_validation._relaxng_cache
_relaxng_cache['tree'] = None
with tools.file_open(get_resource_path('app_common', 'rng', 'tree_view.rng')) as frng:
    try:
        text = frng.read()
        # with tools.file_open('addons/base/rng/common.rng') as common_rng:
        #     common_txt = common_rng.read()
        #     start_pos = common_txt.find('<rng:grammar')
        #     start_pos = common_txt.find('>', start_pos)
        #     end_pos = common_txt.find('</rng:grammar>')
        #     common_content = common_txt[start_pos + 1: end_pos]
        #
        #     # 从14中学习，最新 common
        #     # <rng:optional><rng:attribute name="kanban_view_ref" />
        #     old_content = '''
        #     <rng:optional><rng:attribute name="kanban_view_ref" /></rng:optional>
        #     '''
        #     new_content = '''
        #         <rng:optional><rng:attribute name="hierarchize"/></rng:optional>
        #         <rng:optional><rng:attribute name="expand"/></rng:optional>
        #         <rng:optional><rng:attribute name="enable_counters"/></rng:optional>
        #         <rng:optional><rng:attribute name="limit"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-bf"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-it"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-danger"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-info"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-muted"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-primary"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-success"/></rng:optional>
        #         <rng:optional><rng:attribute name="decoration-warning"/></rng:optional>
        #         <rng:optional><rng:attribute name="kanban_view_ref" /></rng:optional>
        #         '''
        #     common_content = common_content.replace(old_content, new_content)
        #     # common 替代
        #     text = text.replace('<rng:include href=\"common.rng\"/>', common_content)
        #     # tree 替代
        #     old_content = '''<rng:ref name="control"/>'''
        #     new_content = '''<rng:element name="header">
        #             <rng:zeroOrMore>
        #                 <rng:ref name="button"/>
        #             </rng:zeroOrMore>
        #             </rng:element>
        #             <rng:ref name="control"/>'''
        #     text = text.replace(old_content, new_content)
        #     # 增加 fx_tree_table 支持
        #     text = text.replace('<rng:optional><rng:attribute name=\"js_class\"/></rng:optional>',
        #                         '<rng:optional><rng:attribute name=\"js_class\"/></rng:optional><rng:optional><rng:attribute name=\"options\"/></rng:optional>')

        tmp_doc = etree.fromstring(text.encode('utf-8'))
        _relaxng_cache['tree'] = etree.RelaxNG(tmp_doc)
        _logger.warning('=========new tree done: %s' % _relaxng_cache['tree'])
    except Exception as error:
        _logger.exception('Failed to load RelaxNG XML schema for views validation, {error}'.format(
            error=error))
        _relaxng_cache['tree'] = None


@validate('tree')
def app_valid_field_in_tree(arch, **kwargs):
    # 增加 header
    return all(
        child.tag in ('field', 'button', 'control', 'groupby', 'header')
        for child in arch.xpath('/tree/*')
    )

view_validation.valid_field_in_tree = app_valid_field_in_tree
