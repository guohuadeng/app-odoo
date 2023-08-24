/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import {ActionDialog} from "@web/webclient/actions/action_dialog";
import {Component, onMounted} from "@odoo/owl";
import {SelectCreateDialog} from "@web/views/view_dialogs/select_create_dialog";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

export class ExpandButton extends Component {
    setup() {
        this.last_size = this.props.getsize();
    }

    dialog_button_extend() {
        this.props.setsize("dialog_full_screen");
        this.render();
    }

    dialog_button_restore() {
        this.props.setsize(this.last_size);
        this.render();
    }
}

ExpandButton.template = "app_odoo_customize.ExpandButton";

Object.assign(ActionDialog.components, {ExpandButton});
SelectCreateDialog.components = Object.assign(SelectCreateDialog.components || {}, {
    ExpandButton,
});
Dialog.components = Object.assign(Dialog.components || {}, {ExpandButton});
// Patch annoying validation method
Dialog.props.size.validate = (s) => ["sm", "md", "lg", "xl", "dialog_full_screen"].includes(s);

//处理 owl patch
patch(Dialog.prototype, "app_odoo_customize.Dialog", {
    setup() {
        this._super.apply(this, arguments);
        const app_system_name = session.app_system_name || "odooApp";
        this.title = app_system_name;
        this.setSize = this.setSize.bind(this);
        this.getSize = this.getSize.bind(this);

        owl.onMounted(() => {
            this.setDrag();
        });
    },

    setSize(size) {
        this.props.size = size;
        this.render();
    },

    getSize() {
        return this.props.size;
    },

    setDrag() {
        var $dl = $('#' + this.id + ' .modal-dialog .modal-content');
        if ($dl)
            $dl.draggable({
                handle: ".modal-header"
            });
    },
});

patch(SelectCreateDialog.prototype, "app_odoo_customize.SelectCreateDialog", {
    setup() {
        this._super.apply(this, arguments);
        const app_system_name = session.app_system_name || "odooApp";
        this.title = app_system_name;
        this.setSize = this.setSize.bind(this);
        this.getSize = this.getSize.bind(this);

        owl.onMounted(() => {
            this.setDrag();
        });
    },

    setSize(size) {
        this.props.size = size;
        this.render();
    },

    getSize() {
        return this.props.size;
    },

    setDrag() {
        var $dl = $('#' + this.id + ' .modal-dialog .modal-content');
        if ($dl)
            $dl.draggable({
                handle: ".modal-header"
            });
    },
});

