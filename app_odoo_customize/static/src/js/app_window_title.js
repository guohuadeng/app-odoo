/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(WebClient.prototype, "app_odoo_customize.WebClient", {
    setup() {
        this._super.apply(this, arguments);
        const app_system_name = session.app_system_name || 'odooApp';
        this.title.setParts({ zopenerp: app_system_name }); // zopenerp is easy to grep
    }
});
