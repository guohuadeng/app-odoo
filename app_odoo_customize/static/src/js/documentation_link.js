/** @odoo-module **/
/* jshint esversion: 6 */
/* author: 欧度智能，https://www.odooai.cn
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
 *
 * Patch the native DocumentationLink widget to use the configurable
 * app_doc_root_url system parameter instead of the hardcoded
 * https://www.odoo.com, so all in-app help links redirect to
 * the user-defined documentation site.
 */

import { patch } from "@web/core/utils/patch";
import { DocumentationLink } from "@web/views/widgets/documentation_link/documentation_link";
import { session } from "@web/session";

const LINK_REGEX = new RegExp("^https?://");

patch(DocumentationLink.prototype, {
    get url() {
        if (LINK_REGEX.test(this.props.path)) {
            return this.props.path;
        }
        const serverVersion = session.server_version_info.includes("final")
            ? `${session.server_version_info[0]}.${session.server_version_info[1]}`.replace(
                  "~",
                  "-"
              )
            : "master";
        const docRootUrl = (session.app_doc_root_url || "https://www.odoo.com").replace(/\/+$/, "");
        const langPrefix = session.bundle_params && session.bundle_params.lang === "zh_CN" ? "/zh_CN" : "";
        return docRootUrl + "/documentation/" + serverVersion + langPrefix + this.props.path;
    },
});
