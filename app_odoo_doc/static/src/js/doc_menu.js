/** @odoo-module **/

import {registry} from '@web/core/registry';
import {useService} from '@web/core/utils/hooks';
import {Component} from '@odoo/owl';


export class DocMenu extends Component {
    // v20（OWL3）：OWL2 的静态 props 声明已废弃 —— owl3 兼容层遇到它会直接抛错
    // 依据 web/static/src/owl2/owl3_compatibility_layer.js:44-48
    static template = 'app_odoo_doc.DocMenu';

    setup() {
        this.orm = useService('orm');           // v20 仍保留 orm 服务：web/static/src/core/orm_plugin.js:413
        this.actionService = useService('action');
    }

    async actionOpenDoc() {
        // v20 action 服务仍有 currentController：web/static/src/core/errors/error_dialogs.js:265
        const action = this.actionService.currentController.action;
        const res_action = await this.orm.call("ir.module.module", "action_xml_go_doc", [], {
            xml_id: action.xml_id,
        });
        this.actionService.doAction(res_action);
    }

}


export const DocSystrayItem = {
    Component: DocMenu,
};

// v20 systray 注册范式与原生一致：web/static/src/webclient/switch_company_menu/switch_company_menu.js:356
registry.category('systray').add('DocMenu', DocSystrayItem, {sequence: 101});
