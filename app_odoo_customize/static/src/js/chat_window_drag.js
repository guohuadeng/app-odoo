/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";

// ---------------------------------------------------------------------------
// ChatWindow Drag & Resize — DOM‑based (MutationObserver)
//
// Instead of patching OWL lifecycle hooks (which may fail depending on
// the component's internal implementation), we watch the live DOM for
// new ``.o-mail-ChatWindow`` elements and attach drag/resize handlers
// directly.  This works with any Odoo version that keeps the root
// class name ``o-mail-ChatWindow``.
// ---------------------------------------------------------------------------

const MIN_WIDTH = 300;   // px
const MIN_HEIGHT = 200;  // px
const RESIZE_HANDLE_CLASS = "o_odoo_customize_chat_resize";       // bottom-right
const RESIZE_HANDLE_LEFT_CLASS = "o_odoo_customize_chat_resize_left"; // bottom-left

// ---------------------------------------------------------------------------
// Single ChatWindow instance helpers
// ---------------------------------------------------------------------------

function normalizePosition(el) {
    const style = el.style;
    const computed = window.getComputedStyle(el);
    if (computed.position === "static" || computed.position === "relative") {
        style.position = "absolute";
    }
    if (!style.left || style.left === "auto") {
        const rect = el.getBoundingClientRect();
        style.left = rect.left + "px";
        style.right = "auto";
    }
    if (!style.top || style.top === "auto") {
        const rect = el.getBoundingClientRect();
        style.top = rect.top + "px";
        style.bottom = "auto";
    }
    const rect = el.getBoundingClientRect();
    if (rect.left < 0) style.left = "0px";
    if (rect.top < 0) style.top = "0px";
    if (rect.right > window.innerWidth) style.left = (window.innerWidth - rect.width) + "px";
}

function attachDragResize(chatWindowEl) {
    if (chatWindowEl.dataset.odooCustomDragInit) return;  // already initialised
    chatWindowEl.dataset.odooCustomDragInit = "1";

    // ----- resize state (scoped to this chatWindow) -----
    let dragInfo = null;
    let resizeInfo = null;  // { startX, startY, startWidth, startHeight, startLeft, edge }
    let docListeners = false;
    let wasDragged = false; // true when mouse actually moved during this drag session

    const onMouseMove = (e) => {
        if (dragInfo) {
            wasDragged = true;
            const dx = e.clientX - dragInfo.startX;
            const dy = e.clientY - dragInfo.startY;
            chatWindowEl.style.left = (dragInfo.startLeft + dx) + "px";
            chatWindowEl.style.top = (dragInfo.startTop + dy) + "px";
        }
        if (resizeInfo) {
            const dx = e.clientX - resizeInfo.startX;
            const dy = e.clientY - resizeInfo.startY;
            if (resizeInfo.edge === "left") {
                // Resizing from left edge: width grows left, left moves with drag
                let newWidth = resizeInfo.startWidth - dx;
                let newLeft = resizeInfo.startLeft + dx;
                if (newWidth < MIN_WIDTH) {
                    newLeft = resizeInfo.startLeft + resizeInfo.startWidth - MIN_WIDTH;
                    newWidth = MIN_WIDTH;
                }
                chatWindowEl.style.width = newWidth + "px";
                chatWindowEl.style.left = newLeft + "px";
            } else {
                // Resizing from right edge (default)
                chatWindowEl.style.width =
                    Math.max(MIN_WIDTH, resizeInfo.startWidth + dx) + "px";
            }
            chatWindowEl.style.height =
                Math.max(MIN_HEIGHT, resizeInfo.startHeight + dy) + "px";
        }
    };

    const onMouseUp = () => {
        if (dragInfo) {
            chatWindowEl.style.transition = "";
            dragInfo = null;
        }
        if (resizeInfo) {
            chatWindowEl.style.transition = "";
            resizeInfo = null;
        }
        if (!dragInfo && !resizeInfo) {
            document.removeEventListener("mousemove", onMouseMove);
            document.removeEventListener("mouseup", onMouseUp);
            docListeners = false;
        }
    };

    const bindDocListeners = () => {
        if (docListeners) return;
        document.addEventListener("mousemove", onMouseMove);
        document.addEventListener("mouseup", onMouseUp);
        docListeners = true;
    };

    // ----- drag (via header) -----
    const header =
        chatWindowEl.querySelector(".o-mail-ChatWindow-header") ||
        chatWindowEl.querySelector(":scope > div:first-child");
    if (header) {
        header.style.cursor = "move";
        header.title = _t("Press to drag the dialog window");
        header.addEventListener("mousedown", (e) => {
            wasDragged = false;
            if (
                e.target.closest(
                    "button, .btn, i.fa, i.oi, input, textarea, select, a"
                )
            ) {
                return;
            }
            e.preventDefault();
            normalizePosition(chatWindowEl);
            const rect = chatWindowEl.getBoundingClientRect();
            dragInfo = {
                startX: e.clientX,
                startY: e.clientY,
                startLeft: rect.left,
                startTop: rect.top,
            };
            chatWindowEl.style.transition = "none";
            bindDocListeners();
        });

        // Prevent the ChatWindow's built-in click handler (which would
        // fold / minimise the window) from firing after a real drag.
        header.addEventListener("click", (e) => {
            if (wasDragged) {
                e.stopImmediatePropagation();
                e.preventDefault();
            }
        }, true);
    }

    // ----- resize handle (bottom-right) -----
    let handleR = chatWindowEl.querySelector("." + RESIZE_HANDLE_CLASS);
    if (!handleR) {
        handleR = document.createElement("div");
        handleR.className = RESIZE_HANDLE_CLASS;
        chatWindowEl.appendChild(handleR);
    }
    handleR.title = _t("Drag to resize the dialog window");
    handleR.addEventListener("mousedown", (e) => {
        e.preventDefault();
        e.stopPropagation();
        normalizePosition(chatWindowEl);
        const rect = chatWindowEl.getBoundingClientRect();
        resizeInfo = {
            startX: e.clientX,
            startY: e.clientY,
            startWidth: rect.width,
            startHeight: rect.height,
            startLeft: rect.left,
            edge: "right",
        };
        chatWindowEl.style.transition = "none";
        bindDocListeners();
    });

    // ----- resize handle (bottom-left) -----
    let handleL = chatWindowEl.querySelector("." + RESIZE_HANDLE_LEFT_CLASS);
    if (!handleL) {
        handleL = document.createElement("div");
        handleL.className = RESIZE_HANDLE_LEFT_CLASS;
        chatWindowEl.appendChild(handleL);
    }
    handleL.title = _t("Drag to resize the dialog window");
    handleL.addEventListener("mousedown", (e) => {
        e.preventDefault();
        e.stopPropagation();
        normalizePosition(chatWindowEl);
        const rect = chatWindowEl.getBoundingClientRect();
        resizeInfo = {
            startX: e.clientX,
            startY: e.clientY,
            startWidth: rect.width,
            startHeight: rect.height,
            startLeft: rect.left,
            edge: "left",
        };
        chatWindowEl.style.transition = "none";
        bindDocListeners();
    });
}

// ---------------------------------------------------------------------------
// Watch for new ChatWindows via MutationObserver
// ---------------------------------------------------------------------------
function startWatching() {
    // Initial scan — catch any ChatWindow already in the DOM
    document.querySelectorAll(".o-mail-ChatWindow").forEach(attachDragResize);

    // Watch for dynamically added ChatWindows
    const observer = new MutationObserver((mutations) => {
        for (const m of mutations) {
            for (const node of m.addedNodes) {
                if (!(node instanceof HTMLElement)) continue;
                // The added node itself might be a ChatWindow
                if (node.matches(".o-mail-ChatWindow")) {
                    attachDragResize(node);
                }
                // Or it may contain ChatWindow descendants
                const children = node.querySelectorAll(".o-mail-ChatWindow");
                children.forEach(attachDragResize);
            }
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
}

// Start when the DOM is ready
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startWatching);
} else {
    startWatching();
}
