/** @odoo-module **/

import {patch} from "@web/core/utils/patch";
import {append} from "@web/core/utils/xml";
import {MailFormCompiler} from "@mail/views/form/form_compiler";
import {FormCompiler} from "@web/views/form/form_compiler";
import {FormController} from "@web/views/form/form_controller";

patch(MailFormCompiler.prototype, "web_chatter_position", {
    /**
     * Patch the visibility of the Sided chatter (`C` above).
     *
     * @override
     */
    compile() {
        const res = this._super.apply(this, arguments);
        const chatterContainerHookXml = res.querySelector(
            ".o_FormRenderer_chatterContainer"
        );
        if (!chatterContainerHookXml) {
            return res;
        }
        // Don't patch anything if the setting is "auto": this is the core behaviour
        if (odoo.web_chatter_position === "auto") {
            return res;
        } else if (odoo.web_chatter_position === "sided") {
            chatterContainerHookXml.setAttribute("t-if", "!hasAttachmentViewer()");
        } else if (odoo.web_chatter_position === "bottom") {
            chatterContainerHookXml.setAttribute("t-if", false);
        }
        return res;
    },
});

patch(FormCompiler.prototype, "web_chatter_position", {
    /**
     * Patch the css classes of the `Form`, to include an extra `h-100` class.
     * Without it, the form sheet will not be full height in some situations,
     * looking a bit weird.
     *
     * @override
     */
    compileForm() {
        const res = this._super.apply(this, arguments);
        if (odoo.web_chatter_position === "sided") {
            const classes = res.getAttribute("t-attf-class");
            res.setAttribute("t-attf-class", `${classes} h-100`);
        }
        return res;
    },
    /**
     * Patch the visibility of bottom chatters (`A` and `B` above).
     * `B` may not exist in some situations, so we ensure it does by creating it.
     *
     * @override
     */
    compile(node, params) {
        const res = this._super.apply(this, arguments);
        const chatterContainerHookXml = res.querySelector(
            ".o_FormRenderer_chatterContainer:not(.o-isInFormSheetBg)"
        );
        if (!chatterContainerHookXml) {
            return res;
        }
        if (chatterContainerHookXml.parentNode.classList.contains("o_form_sheet")) {
            return res;
        }
        // Don't patch anything if the setting is "auto": this is the core behaviour
        if (odoo.web_chatter_position === "auto") {
            return res;
            // For "sided", we have to remote the bottom chatter
            // (except if there is an attachment viewer, as we have to force bottom)
        } else if (odoo.web_chatter_position === "sided") {
            const formSheetBgXml = res.querySelector(".o_form_sheet_bg");
            if (!formSheetBgXml) {
                return res;
            }
            chatterContainerHookXml.setAttribute("t-if", false);
            // For "bottom", we keep the chatter in the form sheet
            // (the one used for the attachment viewer case)
            // If it's not there, we create it.
        } else if (odoo.web_chatter_position === "bottom") {
            if (params.hasAttachmentViewerInArch) {
                const sheetBgChatterContainerHookXml = res.querySelector(
                    ".o_FormRenderer_chatterContainer.o-isInFormSheetBg"
                );
                sheetBgChatterContainerHookXml.setAttribute("t-if", true);
                chatterContainerHookXml.setAttribute("t-if", false);
            } else {
                const formSheetBgXml = res.querySelector(".o_form_sheet_bg");
                if (!formSheetBgXml) {
                    return res;
                }
                const sheetBgChatterContainerHookXml =
                    chatterContainerHookXml.cloneNode(true);
                sheetBgChatterContainerHookXml.classList.add("o-isInFormSheetBg");
                sheetBgChatterContainerHookXml.setAttribute("t-if", true);
                append(formSheetBgXml, sheetBgChatterContainerHookXml);
                const sheetBgChatterContainerXml =
                    sheetBgChatterContainerHookXml.querySelector("ChatterContainer");
                sheetBgChatterContainerXml.setAttribute("isInFormSheetBg", "true");
                chatterContainerHookXml.setAttribute("t-if", false);
            }
        }
        return res;
    },
});

patch(FormController.prototype, "web_chatter_position", {
    /**
     * Patch the css classes of the form container, to include an extra `flex-row` class.
     * Without it, it'd go for flex columns direction and it won't look good.
     *
     * @override
     */
    get className() {
        const result = this._super();
        if (odoo.web_chatter_position === "sided") {
            result["flex-row"] = true;
        }
        return result;
    },
});