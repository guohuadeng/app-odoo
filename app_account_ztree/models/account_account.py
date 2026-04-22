# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountAccount(models.Model):
    _inherit = ['account.account']
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'code'

    parent_id = fields.Many2one(
        'account.account', string='Parent Chart', index=True, ondelete='restrict',
    )
    child_ids = fields.One2many('account.account', 'parent_id', string='Child Chart')
    parent_path = fields.Char(index=True)
    # todo: view 类型只用于上级，不可在凭证中选择使用。  odoo 中使用 _compute_account_type 处理是找不到自动设置为 其上级科目
    # 故暂时不增加此类型
    # account_type = fields.fields.Selection(selection_add=[
    #     ('view', 'View Only'),
    # ])
    
    # ----------------------------------------------------------
    # Helper
    # ----------------------------------------------------------

    def _get_parent_from_code(self, code, company):
        """Determine the parent account based on code and delimiter.

        Supports two hierarchy styles:
        - Delimiter-based (e.g. '1122.01.03' -> parent '1122.01')
        - Fixed-length   (e.g. '112201'       -> parent '1122')

        :param code:    account code string
        :param company: res.company record to scope the search
        :return:        account.account recordset (empty if no parent found)
        """
        if not code or not company:
            return self.env['account.account'].browse()

        delimiter = company.coa_delimiter or ''
        parent_code = False

        if delimiter and delimiter in code:
            parts = code.rsplit(delimiter, 1)
            if len(parts) > 1 and parts[1]:
                parent_code = parts[0]
        elif len(code) > 2:
            parent_code = code[:len(code) - 2]

        if not parent_code:
            return self.env['account.account'].browse()

        parent = self.search([
            ('company_ids', '=', company.id),
            ('code', '=', parent_code),
        ], limit=1)
        return parent

    # ----------------------------------------------------------
    # CRUD overrides
    # ----------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        """Auto-set parent_id based on code when creating accounts."""
        records = super().create(vals_list)
        for rec in records:
            if rec.code and not rec.parent_id:
                company = rec.company_ids[:1] or self.env.company
                parent = rec._get_parent_from_code(rec.code, company)
                if parent:
                    rec.parent_id = parent.id
        return records

    def write(self, vals):
        """When code changes, block if children exist; then update parent_id."""
        old_codes = {}
        if 'code' in vals:
            old_codes = {rec.id: rec.code for rec in self}
            for rec in self:
                if rec.code != vals['code'] and rec.child_ids:
                    raise UserError(
                        _("Cannot change the code of account '%s' because it has child accounts. "
                          "Please reassign or remove the child accounts first.")
                        % rec.display_name
                    )

        res = super().write(vals)

        if 'code' in vals:
            for rec in self:
                if old_codes.get(rec.id) != rec.code:
                    company = rec.company_ids[:1] or self.env.company
                    parent = rec._get_parent_from_code(rec.code, company)
                    new_parent_id = parent.id if parent else False
                    if rec.parent_id.id != new_parent_id:
                        rec.parent_id = new_parent_id

        return res

    @api.ondelete(at_uninstall=False)
    def _unlink_except_has_children(self):
        """Prevent deletion of accounts that have child accounts."""
        for rec in self:
            if rec.child_ids:
                raise UserError(
                    _("Cannot delete account '%s' because it has child accounts. "
                      "Please delete or reassign the child accounts first.")
                    % rec.display_name
                )

    # ----------------------------------------------------------
    # Existing methods
    # ----------------------------------------------------------

    @api.model
    def _search_new_account_code(self, start_code, cache=None):
        res = super()._search_new_account_code(start_code, cache)
        return res

    def refresh_account_parent(self, company=None):
        """Batch refresh parent_id for all accounts based on their codes."""
        if not company:
            company = self.env.user.company_id
        self = self.filtered(lambda r: r.code and len(r.code) > 2).sorted(key=lambda r: r.code)
        done = 0
        # 分隔符 delimiter，用友为""，金蝶为 "."，注意odoo中一级科目，现金默认定义是4位头，银行是6位头
        # 我们使用 用友的多级科目方式，自动生成下级，此处直接覆盖原生
        delimiter = company.coa_delimiter or ''
        for rec in self:
            parent = rec._get_parent_from_code(rec.code, company)
            if parent and rec.parent_id != parent:
                rec.write({'parent_id': parent.id})
                done += 1

        return {
            'effect': {
                'fadeout': 'fast',
                'message': _('Update parent account chart done.<br/>【%s】 records updated.' % done),
                'img_url': '/web/image/%s/%s/image_1024' % (self.env.user._name,
                                                            self.env.user.id) if self.env.user.image_1024 else '/web/static/src/img/smile.svg',
                'type': 'rainbow_man',
            }
        }
