# # Author: Damien Crier
# # Copyright 2017 Camptocamp SA
# # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
from odoo import api, models


class ProcurementGroup(models.Model):
    _inherit = "procurement.group"

    @api.model
    def _is_subcontracted_service(self, product_id):
        return (product_id.type == 'service' and
                product_id.property_subcontracted_service or
                False)

    @api.model
    def _get_rule(self, product_id, location_id, values):
        res = super()._get_rule(product_id, location_id, values)
        if not res:
            if self._is_subcontracted_service(product_id):
                rule_id = location_id.get_warehouse().\
                    subcontracting_service_proc_rule_id
                if rule_id:
                    return rule_id
        return res
