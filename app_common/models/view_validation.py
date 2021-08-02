# -*- coding: utf-8 -*-

import ast
from odoo.tools import view_validation
from odoo.tools.view_validation import get_attrs_field_names as old_gafn
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
    'bg-danger',
    'bg-info',
    'bg-muted',
    'bg-primary',
    'bg-success',
    'bg-warning',
}

def app_get_attrs_field_names(env, arch, model, editable):
    result = []

    def add_bg(node, model, editable, get=old_gafn.get_name):
        for key, val in node.items():
            if not val:
                continue
            if key in ATTRS_WITH_FIELD_NAMES2:
                old_gafn.process_expr(val, get, key, val)

    res = old_gafn(arch, model, editable)
    add_bg(arch, model, editable)
    res += result
    return res

# 使用猴子补丁方式更新
view_validation.get_attrs_field_names = app_get_attrs_field_names
