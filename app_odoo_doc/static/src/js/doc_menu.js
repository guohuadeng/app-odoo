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
        // 但控制器栈可能为空：直接打开 /odoo（应用宫格/命令中心）或 POS 等全屏客户端动作时，
        // _getCurrentController 返回 null（web/static/src/webclient/actions/action_plugin.js:358），
        // 直接取 .action 就报 Cannot read properties of null。
        // 此时传空 xml_id 即可：后端 action_xml_go_doc 会回退到 base 文档。
        const controller = this.actionService.currentController;
        const xmlId = (controller && controller.action && controller.action.xml_id) || null;
        const res_action = await this.orm.call("ir.module.module", "action_xml_go_doc", [], {
            xml_id: xmlId,
        });
        this.actionService.doAction(res_action);
    }

}


export const DocSystrayItem = {
    Component: DocMenu,
};

// v20 systray 注册范式与原生一致：web/static/src/webclient/switch_company_menu/switch_company_menu.js:356
registry.category('systray').add('DocMenu', DocSystrayItem, {sequence: 101});
