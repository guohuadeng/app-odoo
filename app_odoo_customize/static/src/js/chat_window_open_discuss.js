/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ChatWindow } from "@mail/core/common/chat_window";

// ---------------------------------------------------------------------------
// "Open in Discuss" quick button on the ChatWindow header (fa-expand).
// Mirrors the native `expand-discuss` thread action:
//   mail/static/src/discuss/core/web/thread_actions.js
// ---------------------------------------------------------------------------
patch(ChatWindow.prototype, {
    openInDiscuss() {
        const thread = this.thread;
        if (!thread || thread.model !== "discuss.channel") {
            return;
        }
        this.env.services.action.doAction(
            {
                type: "ir.actions.client",
                tag: "mail.action_discuss",
            },
            {
                clearBreadcrumbs: false,
                additionalContext: { active_id: thread.id },
            }
        );
    },
});
