/** @odoo-module **/

import { ErrorDialog, RPCErrorDialog, ClientErrorDialog, NetworkErrorDialog } from "@web/core/errors/error_dialogs";
import { _t } from "@web/core/l10n/translation";
import { browser } from "@web/core/browser/browser";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";

/**
 * 扩展ErrorDialog，添加提交错误的功能
 */

patch(ErrorDialog.prototype, {
    setup() {
        super.setup(...arguments);
        this.action = useService("action");
        this.notification = useService("notification");
    },

    async onSubmitError() {
        const issueUrl = browser.location ? browser.location.href : 'http://localhost';
        const errorTitle = this.props.name || "Error";
        const errorData = this.traceback;

        this.action.doAction({
            type: 'ir.actions.act_window',
            res_model: 'error.submit.wizard',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new',
            context: {
                default_issue_url: issueUrl,
                default_issue_title: errorTitle,
                default_issue_body: errorData,
            },
        });
    },
});

// 同样扩展RPCErrorDialog
patch(RPCErrorDialog.prototype, {
    setup() {
        super.setup(...arguments);
    }
});

patch(ClientErrorDialog.prototype, {
    setup() {
        super.setup(...arguments);
    }
});

patch(NetworkErrorDialog.prototype, {
    setup() {
        super.setup(...arguments);
    }
});
