# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    chatter_position = fields.Selection([
        ("auto", "Responsive"),
        ("bottom", "Bottom"),
        ("sided", "Sided"),
        ], string='Chatter Position', default="bottom")

    # v20 断点：SELF_READABLE_FIELDS / SELF_WRITEABLE_FIELDS 两个类属性在 v20 已被整体删除
    # （v20 全仓 odoo/ 与 addons_ent/ 对这两个名字零命中；v18 在 base/models/res_users.py 里
    #  用它们界定普通用户自助可读/可写的字段）。原来的
    #   @property def SELF_READABLE_FIELDS(self): return super().SELF_READABLE_FIELDS + [...]
    # 在 v20 里 super() 上没有该属性 ⇒ 一旦有人访问就 AttributeError，而访问点通常在
    # 框架或第三方模块里，属于「装得上、跑到就炸」的死代码，整段删除。
    #
    # v20 里「用户自己改自己的哪些字段」由 ir.model.access 的 SELF 权限（ir.access 的
    # kind=permission + 空 group）承担，不再有字段白名单需要扩展；
    # 本模块的 chatter_position 会随 res.users 的自有权限一起可写，无需额外声明。

    # ----------------------------------------------------------
    # 某用户失效场景处理
    # ----------------------------------------------------------

    @api.model
    def _get_invalidation_fields(self):
        """扩大失效字段集合，使 chatter_position 变更时同步刷新缓存
           —— v20 原生机制未变（base/models/res_users.py:729-731 用它决定要不要
              `env.transaction.invalidate_ormcache()`），与 Odoo 原生 'lang' 字段同一套写法。
        """
        return super()._get_invalidation_fields() | {'chatter_position'}
