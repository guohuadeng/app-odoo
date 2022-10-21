/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(Dialog.prototype, "app_odoo_customize.Dialog", {
    setup() {
        this._super.apply(this, arguments);
        const app_system_name = session.app_system_name || "odooApp";
        this.title = app_system_name;
    },
    // mounted() {
    //     //todo: 没用，不能用 jq的处理方式
    //     this._super.apply(this, arguments);
    //     var $dl = this.__owl__.vnode ? this.__owl__.vnode.elm : null;
    //     var $ml = $dl.children[0].children[0].children[0];
    //     $ml.draggable({
    //         handle: ".modal-header"
    //     });
    // },
});

