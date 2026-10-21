/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

// 企业版/Studio 在 systray 中注册的键名：
// PromoteStudioSystrayItem - web_enterprise 的 Odoo Studio 促销角标（未装 web_studio 时存在）
// StudioSystrayItem        - web_studio 的 Studio 切换按钮（已装 web_studio 时存在）
// 本模块不依赖 web_enterprise/web_studio，仅按注册键过滤，两个模块未安装时不受影响。
const STUDIO_SYSTRAY_KEYS = ["PromoteStudioSystrayItem", "StudioSystrayItem"];

patch(NavBar.prototype, {
    get systrayItems() {
        // 只由 app_show_studio 控制：为真则显示当前存在的 Studio 角标，否则隐藏
        const showStudio = Boolean(session.app_show_studio);
        return super.systrayItems.filter(
            (item) => !STUDIO_SYSTRAY_KEYS.includes(item.key) || showStudio
        );
    },
});
