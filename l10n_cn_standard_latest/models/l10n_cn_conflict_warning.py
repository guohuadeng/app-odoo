# -*- coding: utf-8 -*-

from odoo import api, models, _

from ..hooks import L10N_CN_CONFLICT_WARNING_PARAM


class L10nCnConflictWarning(models.AbstractModel):
    _name = 'l10n.cn.conflict.warning'
    _description = 'L10n CN Module Conflict Warning'

    @api.model
    def get_pending_warning(self):
        """
        读取并清除安装时写入的 l10n_cn 冲突警告标记。
        仅在标记存在且 l10n_cn 仍处于已安装状态时返回提示内容，保证只提示一次。
        非系统管理员不读取也不清除标记，留给管理员登录时提示。
        """
        if not self.env.user.has_group('base.group_system'):
            return False
        params = self.env['ir.config_parameter'].sudo()
        if not params.get_bool(L10N_CN_CONFLICT_WARNING_PARAM):
            return False
        params.set_bool(L10N_CN_CONFLICT_WARNING_PARAM, False)

        l10n_cn = self.env['ir.module.module'].sudo().search(
            [('name', '=', 'l10n_cn'), ('state', '=', 'installed')], limit=1)
        if not l10n_cn:
            return False

        return {
            'title': _('Module Conflict Warning'),
            'message': _(
                'The "l10n_cn" module is installed and may conflict with '
                '"l10n_cn_standard_latest": invoice fields may be duplicated. '
                'It is recommended to uninstall "l10n_cn".'
            ),
        }
