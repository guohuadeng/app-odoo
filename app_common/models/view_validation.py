# -*- coding: utf-8 -*-

import ast
from odoo.tools import view_validation
from odoo.tools.view_validation import get_attrs_field_names as old_gafn
from odoo.tools.view_validation import _get_attrs_symbols
import logging

_logger = logging.getLogger(__name__)

ATTRS_WITH_FIELD_NAMES2 = {
    'context',
    'domain',
    'decoration-bf',
    'decoration-it',
    'decoration-danger',
    'decoration-info',
    'decoration-muted',
    'decoration-primary',
    'decoration-success',
    'decoration-warning',
    'decoration-black',
    'decoration-white',
    'bg-danger',
    'bg-info',
    'bg-muted',
    'bg-primary',
    'bg-success',
    'bg-warning',
    'bg-black',
    'bg-white',
}

def app_get_attrs_field_names(env, arch, model, editable):
    symbols = _get_attrs_symbols() | {None}
    result = []

    def get_name(node):
        """ return the name from an AST node, or None """
        if isinstance(node, ast.Name):
            return node.id

    def process_expr(expr, get, key, val):
        """ parse `expr` and collect triples """
        for node in ast.walk(ast.parse(expr.strip(), mode='eval')):
            name = get(node)
            if name not in symbols:
                result.append((name, key, val))
                
    def add_bg(node, model, editable, get=get_name):
        for key, val in node.items():
            if not val:
                continue
            if key in ATTRS_WITH_FIELD_NAMES2:
                process_expr(val, get, key, val)

    res = old_gafn(env, arch, model, editable)
    add_bg(arch, model, editable)
    res += result
    return res

# 使用猴子补丁方式更新
view_validation.get_attrs_field_names = app_get_attrs_field_names
