# -*- coding: utf-8 -*-

# Created on 2018-11-28
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.odooai.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.odooai.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.odooai.cn/odoo10_developer_document_offline/
# description:

import csv
import json
import logging
import os

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class AccountAccount(models.Model):
    _inherit = ['account.account']
    # 相关方法处理移至 app_account_ztree

    def _get_account_code_from_csv(self, xml_id):
        if not xml_id:
            return None

        # 提取csv_id部分 (account.1_account_1001 -> account_1001)
        parts = xml_id.split('_', 1)
        if len(parts) < 2:
            return None
        csv_id = parts[1]

        module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(module_path, 'data', 'template', 'account.account-cn_standard.csv')

        if not os.path.exists(csv_path):
            return None

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('id') == csv_id:
                        code = row.get('code', '').strip()
                        # 确保返回非空字符串，避免Odoo将空字符串视为False
                        return code if code else None
        except Exception as e:
            _logger.warning(f"Error reading CSV file: {e}")

        return None

    def action_update_account_codes_from_csv(self):
        ir_model_data = self.env['ir.model.data'].sudo()

        updates = {}  # {account_id: (company_id, code)}

        for account in self:
            company_id = account.company_ids[0].id if account.company_ids else self.env.company.id

            # 检查是否已有code_store值
            existing_code = False
            if account.code_store:
                try:
                    code_store_dict = json.loads(account.code_store) if isinstance(account.code_store, str) else account.code_store
                    if isinstance(code_store_dict, dict) and str(company_id) in code_store_dict:
                        existing_code = bool(code_store_dict[str(company_id)])
                except (json.JSONDecodeError, TypeError):
                    existing_code = False

            if not existing_code:
                xml_ids = ir_model_data.search_read([
                    ('model', '=', 'account.account'),
                    ('res_id', '=', account.id)
                ], ['module', 'name'])

                if xml_ids:
                    xml_id = f"{xml_ids[0]['module']}.{xml_ids[0]['name']}"
                    code = self._get_account_code_from_csv(xml_id)

                    if code and isinstance(code, str) and code.strip():
                        updates[account.id] = (company_id, code.strip())

        upd_count = 0
        if updates:
            _logger.info(f"Starting to update {len(updates)} account codes from CSV using SQL")

            # 使用SQL直接更新code_store，完全绕过ORM计算字段机制
            batch_size = 100
            account_ids = list(updates.keys())

            for i in range(0, len(account_ids), batch_size):
                batch_ids = account_ids[i:i + batch_size]

                case_parts = []
                ids_list = []
                for account_id in batch_ids:
                    company_id, code = updates[account_id]
                    code_store_json = json.dumps({str(company_id): code})
                    safe_json = code_store_json.replace("'", "''")
                    case_parts.append(f"WHEN {account_id} THEN '{safe_json}'::jsonb")
                    ids_list.append(str(account_id))

                if case_parts:
                    query = f"""
                        UPDATE account_account
                        SET code_store = CASE id {' '.join(case_parts)} END
                        WHERE id IN ({','.join(ids_list)})
                    """
                    try:
                        self.env.cr.execute(query)
                        upd_count += len(batch_ids)
                        _logger.debug(f"Updated batch {i//batch_size + 1} with {len(batch_ids)} accounts")
                    except Exception as e:
                        _logger.error(f"Failed to execute batch update: {e}")
                        continue

            self.env.cr.commit()
            _logger.info(f"Successfully updated {upd_count} account codes from CSV")

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': _('Updated %d account codes successfully') % upd_count,
                'type': 'success',
                'sticky': False,
                'next': {
                    'type': 'ir.actions.client',
                    'tag': 'soft_reload',
                },
            }
        }
