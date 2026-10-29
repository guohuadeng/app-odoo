/** @odoo-module **/
/* jshint esversion: 6 */

import { _t } from "@web/core/l10n/translation";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { router } from "@web/core/browser/router";
import { patch } from "@web/core/utils/patch";
import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { session } from "@web/session";
import { user } from "@web/core/user";
import { useService } from "@web/core/utils/hooks";
const userMenuRegistry = registry.category("user_menuitems");

patch(UserMenu.prototype, {
    setup() {
        super.setup();
        "use strict";
        // self.companyService = useService("company");
        let self = this;
        self.orm = useService("orm");
        self.app_show_lang = session.app_show_lang;
        self.app_lang_list = session.app_lang_list;
        self.user_lang = session.bundle_params.lang;

        userMenuRegistry.add("refresh_current", refresh_current, {'force': true});

        if (session.app_show_lang) {
            userMenuRegistry.add("separator1", separator1, {'force': true});
        }
        if (session.app_show_debug && session.is_erp_manager) {
            userMenuRegistry.add("debug", debugItem, {'force': true})
                .add("asset_asset", activateAssetsDebugging, {'force': true})
                .add("leave_debug", leaveDebugMode, {'force': true})
                .add("separator10", separator10, {'force': true});
        }
        if (session.app_show_documentation) {
            userMenuRegistry.add("documentation", documentationItem, {'force': true});
        }
        if (session.app_show_support) {
            try {
                userMenuRegistry.add("support", supportItem, {'force': true});
            } catch (err) {
                ;
            }
        } else if (userMenuRegistry.get('support', false)) {
            try {
                userMenuRegistry.remove("support");
            } catch (err) {
                ;
            }
        }
        if (session.app_show_account) {
            userMenuRegistry.add("odoo_account", odooAccountItem, {'force': true});
        } else if (userMenuRegistry.get('odoo_account', false)){
            try {
                userMenuRegistry.remove("odoo_account");
            } catch (err) {
                ;
            }
        }
    },

    async setLang(lang_code) {
        "use strict";
        // alert(lang_code);
        let self = this;
        browser.clearTimeout(self.toggleTimer);
        if (self.user_lang !== lang_code) {
            const res = await self.orm.call("res.users", "write", [
                user.userId, {'lang': lang_code}
            ]);
            location.reload();
            // 调用 action , 要先定义 self.action = useService("action")
            // self.action.action({
            //     type: 'ir.actions.client',
            //     tag: 'reload_context',
            // });
        }
    }
});

function debugItem(env) {
    "use strict";
    return {
        type: "item",
        id: "debug",
        description: _t("Activate the developer mode"),
        callback: () => {
            router.pushState({ debug: 1 }, { reload: true });
        },
        show:  () => !env.debug || !env.debug.includes("assets"),
        sequence: 5,
    };
}

function activateAssetsDebugging(env) {
    "use strict";
    return {
        type: "item",
        description: _t("Activate Assets Debugging"),
        callback: () => {
            router.pushState({ debug: 'assets' }, { reload: true });
        },
        show:  () => !env.debug.includes("assets"),
        sequence: 6,
    };
}

function leaveDebugMode(env) {
    "use strict";
    return {
        type: "item",
        description: _t("Leave the Developer Tools"),
        callback: () => {
            router.pushState({ debug: 0 }, { reload: true });
        },
        show:  () => env.debug,
        sequence: 7,
    };
}

function separator1() {
    "use strict";
    return {
        type: "separator",
        sequence: 1,
    };
}

function separator10() {
    "use strict";
    return {
        type: "separator",
        sequence: 10,
    };
}

function documentationItem(env) {
    "use strict";
    const documentationURL = session.app_documentation_url;

    return {
        type: "item",
        id: "documentation",
        description: _t("Documentation"),
        href: documentationURL,
        callback: () => {
            browser.open(documentationURL, "_blank");
        },
        sequence: 21,
    };
}

function supportItem(env) {
    "use strict";
    const url = session.app_support_url;
    return {
        type: "item",
        id: "support",
        description: _t("Support"),
        href: url,
        callback: (ev) => {
            browser.open(url, "_blank");
        },
        sequence: 22,
    };
}

function odooAccountItem(env) {
    "use strict";
    const app_account_title = session.app_account_title;
    const app_account_url = session.app_account_url;
    const dialog = env.services.dialog;
    return {
        type: "item",
        id: "account",
        description: _t(app_account_title),
        href: app_account_url,
        callback: () => {
            dialog.add(ConfirmationDialog, {
                title: _t("Confirm Navigation"),
                body: _t("You are about to leave the current system and go to the OdooAI Service Center. Do you want to continue?"),
                confirmLabel: _t("Confirm"),
                cancelLabel: _t("Cancel"),
                confirm: () => {
                    top.location.href = app_account_url;
                },
            });
            // top.location.href = app_account_url;
            // browser.open(app_account_url, "_blank");
        },
        sequence: 60,
    };
}

function refresh_current(env) {
    //移动端，主要为了小程序
    "use strict";
    const ui = env.services.ui;
    return {
        type: "item",
        id: "refresh_current",
        description: _t("Refresh Page"),
        hide: ui.isSmall,
        callback: () => {
            location.reload();
        },
        sequence: 58,
    };
}
