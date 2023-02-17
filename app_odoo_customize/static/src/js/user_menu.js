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
        userMenuRegistry.remove("debug");
        userMenuRegistry.remove("asset_asset");
        userMenuRegistry.remove("leave_debug");
        userMenuRegistry.remove("separator0");
        if (session.app_show_debug) {
            userMenuRegistry.add("debug", debugItem)
                .add("asset_asset", activateAssetsDebugging)
                .add("leave_debug", leaveDebugMode)
                .add("separator0", separator8)
        }
        userMenuRegistry.remove("documentation");
        if (session.app_show_documentation) {
            userMenuRegistry.add("documentation", documentationItem);
        }
        userMenuRegistry.remove("support");
        if (session.app_show_support) {
            userMenuRegistry.add("support", supportItem)
        }
        userMenuRegistry.remove("odoo_account");
        if (session.app_show_account) {
            userMenuRegistry.add("odoo_account", odooAccountItem);
        }
        // this.rpc = useService("rpc");
        // todo: 处理语言列表，rpc取值，同上处理 userMenuRegistry.add("slang_"+语言代码, debugItem(语言代码), env)
        // todo: 语言图片的处理，正常直接参考 Shortcuts 的处理，直接生成 html代码即可。
        // Shortcuts不成就可以扩展 @web/webclient/user_menu/user_menu， 参考 CheckBox 的处理。建议直接CheckBox这个类型改，增加个 element.img的处理，选中的语言就是 ischecked的
        //
        //         return env.services.rpc("/web/action/load", {
        //             action_id: actionID,
        //             additional_context: context,
        //         });
        /*

            self._rpc({
                model: 'res.lang',
                method: 'search_read',
                domain: [],
                fields: ['name', 'code'],
                lazy: false,
            }).then(function (res) {
                _.each(res, function (lang) {
                    var a = '';
                    if (lang['code'] === session.user_context.lang) {
                        a = '<i class="fa fa-check"></i>';
                    } else {
                        a = '';
                    }
                    lang_list += '<a role="menuitem" href="#" class="dropdown-item" data-lang-menu="lang" data-lang-id="' + lang['code']
                        + '"><img class="flag" src="app_odoo_customize/static/src/img/flags/' + lang['code'] + '.png"/>' + lang['name'] + a + '</a>';
                });
                lang_list += '<div role="separator" class="dropdown-divider"/>';
                setTimeout( function() {
                    $('switch-lang').replaceWith(lang_list);
                }, 1000);
            })

         */
    },
    // getElements() {
    //     var ret = this._super.apply(this, arguments);
    //     return ret;
    // },
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

function separator8() {
    return {
        type: "separator",
        sequence: 8,
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
        sequence: 10,
    };
}

function supportItem(env) {
    const url = session.app_support_url;
    return {
        type: "item",
        id: "support",
        description: env._t("Support"),
        href: url,
        callback: () => {
            browser.open(url, "_blank");
        },
        sequence: 20,
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
