# -*- coding: utf-8 -*-

from odoo.fields import Field, resolve_mro
from odoo.fields import Selection as oldSelection
from odoo.tools import merge_sequences
import logging

_logger = logging.getLogger(__name__)

class Selection(Field):
    def _setup_attrs_app(self, model, name):
        Field._setup_attrs(self, model, name)

        # determine selection (applying 'selection_add' extensions)
        values = None
        labels = {}

        for field in reversed(resolve_mro(model, name, self._can_setup_from)):
            # We cannot use field.selection or field.selection_add here
            # because those attributes are overridden by ``_setup_attrs``.
            if 'selection' in field.args:
                selection = field.args['selection']
                if isinstance(selection, list):
                    if (
                        values is not None
                        and values != [kv[0] for kv in selection]
                    ):
                        _logger.debug("%s: selection=%r overrides existing selection; use selection_add instead", self, selection)
                    values = [kv[0] for kv in selection]
                    labels = dict(selection)
                else:
                    self.selection = selection
                    values = None
                    labels = {}

            if 'selection_add' in field.args:
                selection_add = field.args['selection_add']
                assert isinstance(selection_add, list), \
                    "%s: selection_add=%r must be a list" % (self, selection_add)
                assert values is not None, \
                    "%s: selection_add=%r on non-list selection %r" % (self, selection_add, self.selection)
                values = merge_sequences(values, [kv[0] for kv in selection_add])
                labels.update(kv for kv in selection_add if len(kv) == 2)

        if values is not None:
            self.selection = [(value, labels[value]) for value in values]

oldSelection._setup_attrs = Selection._setup_attrs_app