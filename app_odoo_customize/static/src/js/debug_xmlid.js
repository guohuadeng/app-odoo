/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { Component, onWillStart, useState } from "@odoo/owl";

const debugRegistry = registry.category("debug");

/**
 * Debug menu component that displays the XML ID (external ID) of the current record
 * with a copy-to-clipboard button.
 */
class XmlIdDebugItem extends Component {
    static template = "app_odoo_customize.XmlIdDebugItem";
    static components = { DropdownItem };
    static props = {
        resModel: { type: String },
        resId: { type: Number },
    };

    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.state = useState({
            xmlid: "",
            loading: true,
        });
        onWillStart(() => this.loadXmlId());
    }

    async loadXmlId() {
        try {
            const result = await this.orm.call(
                this.props.resModel,
                "get_metadata",
                [[this.props.resId]]
            );
            const metadata = result[0];
            if (metadata) {
                this.state.xmlid = metadata.xmlid || "";
            }
        } catch (e) {
            this.state.xmlid = "";
        }
        this.state.loading = false;
    }

    async copyXmlId(ev) {
        ev.stopPropagation();
        ev.preventDefault();
        if (!this.state.xmlid) {
            return;
        }
        try {
            await navigator.clipboard.writeText(this.state.xmlid);
        } catch (e) {
            // Fallback for non-secure contexts
            const textArea = document.createElement("textarea");
            textArea.value = this.state.xmlid;
            textArea.style.position = "fixed";
            textArea.style.opacity = "0";
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand("copy");
            document.body.removeChild(textArea);
        }
        this.notification.add(
            _t("XML ID copied: %(xmlid)s", { xmlid: this.state.xmlid }),
            { type: "info" }
        );
    }
}

/**
 * Debug menu item factory: shows XML ID with copy button in the Record section,
 * right below the Metadata item (sequence 110).
 */
export function xmlIdItem({ component }) {
    const resId = component.model.root.resId;
    if (!resId) {
        return null;
    }
    return {
        type: "component",
        Component: XmlIdDebugItem,
        props: {
            resModel: component.props.resModel,
            resId: resId,
        },
        sequence: 115,
        section: "record",
    };
}

debugRegistry.category("form").add("xmlIdItem", xmlIdItem);
