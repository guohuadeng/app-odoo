# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, tools, _

import operator

class IrModule(models.Model):
    _inherit = 'ir.module.module'

    # attention: Incorrect field names !!
    #   installed_version refers the latest version (the one on disk)
    #   latest_version refers the installed version (the one in database)
    #   published_version refers the version available on the repository
    # installed_version = fields.Char('Latest Version', compute='_get_latest_version')
    # latest_version = fields.Char('Installed Version', readonly=True)

    local_updatable = fields.Boolean('Local updatable', compute='_get_latest_version', default=False, store=True)

    def module_multi_uninstall(self):
        """ Perform the various steps required to uninstall a module completely
            including the deletion of all database structures created by the module:
            tables, columns, constraints, etc.
        """
        modules = self.browse(self.env.context.get('active_ids'))
        [module.button_immediate_uninstall() for module in modules if module not in ['base', 'web']]


    @api.depends('name')
    def _get_latest_version(self):
        super(IrModule, self)._get_latest_version()
        for rec in self:
            rec.local_updatable = False
            if rec.installed_version and rec.latest_version and operator.gt(rec.installed_version, rec.latest_version):
                rec.local_updatable = True
