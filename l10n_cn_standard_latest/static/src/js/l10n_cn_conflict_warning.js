import { registry } from "@web/core/registry";

/**
 * 后台加载后查询安装时写入的 l10n_cn 冲突警告。
 * 有警告时弹出 sticky 通知（不会自动消失，需用户手动关闭）。
 */
export const l10nCnConflictWarningService = {
    dependencies: ["notification", "orm"],

    start(env, { notification, orm }) {
        orm.silent
            .call("l10n.cn.conflict.warning", "get_pending_warning", [])
            .then((warning) => {
                if (!warning) {
                    return;
                }
                notification.add(warning.message, {
                    title: warning.title,
                    type: "warning",
                    sticky: true,
                });
            })
            .catch((error) => {
                console.warn("l10n_cn conflict warning check failed:", error);
            });
    },
};

registry.category("services").add("l10n_cn_conflict_warning", l10nCnConflictWarningService);
