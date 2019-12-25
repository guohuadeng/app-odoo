# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openupgradelib import openupgrade
from openupgradelib import openupgrade_90


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    column = openupgrade.get_legacy_name('logo')
    if openupgrade.column_exists(env.cr, 'product_brand', column):
        openupgrade_90.convert_binary_field_to_attachment(
            env, {'product.brand': [('logo', None)]},
        )
