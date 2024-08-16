/** @odoo-module **/
// 以下为参考 17 ，仅16需要

import { patch } from "@web/core/utils/patch";
import { EnterpriseNavBar } from "@web_enterprise/webclient/navbar/navbar";

patch(EnterpriseNavBar.prototype, "appEnterpriseNavBar", {
  setup() {
    this._super(...arguments);
    this._busToggledCallback = () => this._updateMenuAppsIcon();
  },

  _updateMenuAppsIcon() {
    this._super(...arguments);
    const menuBrandIcon = this.navRef.el.querySelector(".o_menu_brand_icon");
    if (menuBrandIcon) {
      menuBrandIcon.classList.toggle("o_hidden", !this.isInApp);
    }
  }
});

