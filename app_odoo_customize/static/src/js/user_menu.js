/** @odoo-module **/

import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { routeToUrl } from "@web/core/browser/router_service";
import { patch } from "@web/core/utils/patch";
import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { session } from "@web/session";
import { useService } from "@web/core/utils/hooks";
const userMenuRegistry = registry.category("user_menuitems");

patch(UserMenu.prototype, "app_odoo_customize.UserMenu", {
    setup() {
        this._super.apply(this, arguments);
        // this.companyService = useService("company");
        this.rpc = useService("rpc");
        this.orm = useService("orm");
        this.app_show_lang = session.app_show_lang;
        this.app_lang_list = session.app_lang_list;
        //todo: 演习 shortCutsItem 中的用法，当前是直接 xml 写了展现

        userMenuRegistry.add("refresh_current", refresh_current, {'force': true});

        if (session.app_show_lang) {
            userMenuRegistry.add("separator1", separator1, {'force': true})
        }
        if (session.app_show_debug && session.is_erp_manager) {
            userMenuRegistry.add("debug", debugItem, {'force': true})
                .add("asset_asset", activateAssetsDebugging, {'force': true})
                .add("leave_debug", leaveDebugMode, {'force': true})
                .add("separator10", separator10, {'force': true})
        }
        if (session.app_show_documentation) {
            userMenuRegistry.add("documentation", documentationItem, {'force': true});
        }
        if (session.app_show_support) {
            try {
                userMenuRegistry.add("support", supportItem, {'force': true})
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
        // alert(lang_code);
        browser.clearTimeout(this.toggleTimer);
        if (this.user.lang !== lang_code) {
            const res = await this.orm.call("res.users", "write", [
                session.uid, {'lang': lang_code}
            ]);
            location.reload();
            // 调用 action , 要先定义 this.action = useService("action")
            // this.action.action({
            //     type: 'ir.actions.client',
            //     tag: 'reload_context',
            // });
        }
    }
});

function debugItem(env) {
    const url_debug = $.param.querystring(window.location.href, 'debug=1');
    return {
        type: "item",
        id: "debug",
        description: env._t("Activate the developer mode"),
        href: url_debug,
        callback: () => {
            browser.open(url_debug, "_self");
        },
        sequence: 5,
    };
}

function activateAssetsDebugging(env) {
    return {
        type: "item",
        description: env._t("Activate Assets Debugging"),
        callback: () => {
            browser.location.search = "?debug=assets";
        },
        sequence: 6,
    };
}

function leaveDebugMode(env) {
    return {
        type: "item",
        description: env._t("Leave the Developer Tools"),
        callback: () => {
            const route = env.services.router.current;
            route.search.debug = "";
            browser.location.href = browser.location.origin + routeToUrl(route);
        },
        sequence: 7,
    };
}

function separator1() {
    return {
        type: "separator",
        sequence: 1,
    };
}

function separator10() {
    return {
        type: "separator",
        sequence: 10,
    };
}

function documentationItem(env) {
    const documentationURL = session.app_documentation_url;
    return {
        type: "item",
        id: "documentation",
        description: env._t("Documentation"),
        href: documentationURL,
        callback: () => {
            browser.open(documentationURL, "_blank");
        },
        sequence: 21,
    };
}

function supportItem(env) {
    const url = session.app_support_url;
    return {
        type: "item",
        id: "support",
        description: env._t("Support"),
        href: url,
        callback: (ev) => {
            browser.open(url, "_blank");
        },
        sequence: 22,
    };
}

function odooAccountItem(env) {
    const app_account_title = session.app_account_title;
    const app_account_url = session.app_account_url;
    return {
        type: "item",
        id: "account",
        description: env._t(app_account_title),
        href: app_account_url,
        callback: () => {
            browser.open(app_account_url, "_blank");
        },
        sequence: 60,
    };
}

function refresh_current(env) {
    return {
        type: "item",
        id: "refresh_current",
        description: env._t("Refresh Page"),
        callback: () => {
            location.reload();
        },
        sequence: 58,
    };
}
