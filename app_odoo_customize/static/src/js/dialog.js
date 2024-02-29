/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(Dialog.prototype, {
    setup() {
        super.setup();
        const app_system_name = session.app_system_name || "odooAi";
        this.title = app_system_name;
        //odoo17 已内置 窗口可拖放
        // owl.onMounted(() => {
        //     this.setDrag();
        // });
    },
});

