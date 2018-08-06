# © 2017 Eficent Business and IT Consulting Services S.L.
#        (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class BomStructureReport(models.AbstractModel):
    _inherit = 'report.mrp.mrp_bom_structure_report'

    @api.model
    def _get_child_vals(self, record, level, qty, uom):
        res = super(BomStructureReport, self)._get_child_vals(
            record, level, qty, uom)
        res['location_name'] = record.location_id.complete_name or ''
        return res
