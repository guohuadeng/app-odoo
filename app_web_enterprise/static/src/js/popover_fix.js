/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Popover } from "@web/core/popover/popover";
import { OVERLAY_SYMBOL } from "@web/core/overlay/overlay_container";

patch(Popover.prototype, {
    /**
     * Fix Odoo Popover#isInside TypeError: Cannot read properties of undefined (reading 'contains').
     *
     * Original implementation uses optional chaining ?.(), but Odoo's asset bundler (minify/transpile)
     * may transpile it to bare method calls under certain targets, causing a crash when the Popover
     * target has been destroyed but the window pointerdown listener was not yet cleaned up.
     *
     * This patch replaces optional chaining with explicit && guards for bulletproof null-safety.
     */
    isInside(target) {
        const targetEl = this.props.target;
        const popoverEl = this.popoverRef?.el;
        const overlay = this.env[OVERLAY_SYMBOL];
        return Boolean(
            (targetEl && targetEl.contains(target)) ||
            (popoverEl && popoverEl.contains(target)) ||
            (overlay && overlay.contains(target))
        );
    },
});
