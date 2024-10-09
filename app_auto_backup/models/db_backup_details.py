# -*- coding: utf-8 -*-

import os

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError


class DbBackupDetails(models.Model):
    _name = 'db.backup.details'
    _description = 'Database Backup Details'

    name = fields.Char(string='Name')
    file_path = fields.Char(string="File Path")
    url = fields.Char(string='URL')
    db_backup_id = fields.Many2one('db.backup', 'Database Backup')
    
    def action_download_file(self):
        self.ensure_one()
        if not self.file_path or not self.url:
            raise UserError(_("File Path or URL not found."))
        else:
            return {
                'type': 'ir.actions.act_url',
                'url': self.url,
                'target': 'new',
            }
            
    def unlink(self):
        for rec in self:
            try:
                if rec.file_path:
                    if os.path.exists(rec.file_path):
                        os.remove(rec.file_path)
            except Exception as e:
                pass
        return super(DbBackupDetails, self).unlink()

    def action_remove_file(self):
        self.ensure_one()
        self.unlink()
