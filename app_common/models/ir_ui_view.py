# -*- coding: utf-8 -*-

from odoo import api, models, tools, SUPERUSER_ID
from odoo.modules.module import get_resource_path
from odoo.tools import view_validation
from odoo.tools.view_validation import _relaxng_cache, validate, _validators
from odoo.tools.safe_eval import safe_eval

from lxml import etree
import logging
_logger = logging.getLogger(__name__)

@validate('tree')
def app_valid_field_in_tree(arch, **kwargs):
    # 增加 header
    return all(
        child.tag in ('field', 'button', 'control', 'groupby', 'header')
        for child in arch.xpath('/tree/*')
    )

def app_relaxng(view_type):
    """ Return a validator for the given view type, or None. """
    if view_type not in _relaxng_cache:
        # tree 特殊
        if view_type == 'tree':
            _file = get_resource_path('app_common', 'rng', 'tree_view.rng')
        else:
            _file = get_resource_path('base', 'rng', '%s_view.rng' % view_type)
        with tools.file_open(_file) as frng:
            try:
                relaxng_doc = etree.parse(frng)
                _relaxng_cache[view_type] = etree.RelaxNG(relaxng_doc)
            except Exception:
                _logger.exception('Failed to load RelaxNG XML schema for views validation')
                _relaxng_cache[view_type] = None
            _logger.error('==================new rng: %s' % _file)
    return _relaxng_cache[view_type]

def app_reset_valid_view(view_type):
    _relaxng_cache = view_validation._relaxng_cache
    for pred in _validators[view_type]:
        # 要pop掉函数 valid_field_in_tree
        if pred.__name__ == 'valid_field_in_tree':
            _validators[view_type].remove(pred)
    try:
        _relaxng_cache.pop(view_type, None)
        _relaxng_cache[view_type] = None
    except Exception:
        pass
    _relaxng_cache[view_type] = app_relaxng(view_type)

app_reset_valid_view('tree')
view_validation.valid_field_in_tree = app_valid_field_in_tree
view_validation.relaxng = app_relaxng

class View(models.Model):
    _inherit = 'ir.ui.view'

    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        view_validation.relaxng = app_relaxng
        # 重置 tree
        app_reset_valid_view('tree')

    # todo: 有可能需要处理增加的 header等标签
    # 直接重写原生方法
    # def transfer_node_to_modifiers(node, modifiers, context=None, in_tree_view=False):
