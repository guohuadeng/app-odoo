/** @odoo-module */

// const { Component, useEffect, onWillStart, onWillUnmount } = owl;
import {session} from "@web/session";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { ZtreeMany2X } from "@app_web_widget_ztree/js/ztree_many2x";
import { Many2OneField, many2OneField } from '@web/views/fields/many2one/many2one_field';

//todo: ztree 继承 import { AutoComplete } from "@web/core/autocomplete/autocomplete";
//field ztree 继承 fieldm2o，优化 xml 并入  Many2XAutocomplete

export class FieldZTree extends Many2OneField {
    setup() {
        super.setup();
        let self = this;
        this.limit = this.SEARCH_MORE_LIMIT ? this.SEARCH_MORE_LIMIT : 1000;
        this.ztree_domain = self.getDomain();
        this.ztree_field = self.props.name;
        this.ztree_model = self.relation;
        this.ztree_parent_key = self.props.ztree_parent_key;
        this.ztree_root_id = self.props.ztree_root_id;
        this.ztree_name_field = self.props.ztree_name_field;
        this.ztree_selected_id = self.props.value ? self.props.value[0] : false;
        this.order = self.props.order;
        this.ztree_expend_level = self.props.ztree_expend_level;
        // onWillStart(async () => {
        //     //数据初始化
        //     await this.willStart();
        // });
        // useEffect(() => this.start());
    }

    get ZtreeMany2xProps() {
        let self = this;
        let res = {
            ...self.Many2XAutocompleteProps,
            data: {
                ztree_domain: self.ztree_domain,
                ztree_field: self.ztree_field,
                ztree_model: self.relation,
                ztree_parent_key: self.ztree_parent_key,
                ztree_root_id: self.ztree_root_id,
                ztree_expend_level: self.ztree_expend_level,
                ztree_name_field: self.props.ztree_name_field,
                ztree_selected_id: self.props.value ? self.props.value[0] : false,
                order: self.order,
            },
        }
        return res;
    }

}


FieldZTree.template = "App.FieldZtree";
FieldZTree.supportedTypes = ["many2one"];
FieldZTree.components = {
    ...Many2OneField.components,
    ZtreeMany2X,
};

//todo: 自行渲染  Many2XAutocomplete ， loadOptionsSource， web.Many2XAutocomplete

FieldZTree.props = {
    ...Many2OneField.props,
    ztree_parent_key: { type: String, optional: true },
    ztree_root_id: { type: Number, optional: true },
    ztree_name_field: { type: String, optional: true },
    order: { type: String, optional: true },
    ztree_expend_level: { type: String, optional: true },
};

FieldZTree.extractProps = ({ field, attrs }) => {
    return {
        ...Many2OneField.extractProps({ field, attrs }),
        ztree_parent_key: attrs.options.ztree_parent_key,
        ztree_root_id: attrs.options.ztree_root_id,
        ztree_name_field: attrs.options.ztree_name_field,
        order: attrs.options.order,
        ztree_expend_level: attrs.options.ztree_expend_level,
    };
};

export const fieldZTree = {
    ...many2OneField,
    component: FieldZTree,
    extractProps({ options }) {
        const props = many2OneField.extractProps(...arguments);
        props.ztree_parent_key = options.ztree_parent_key;
        props.ztree_root_id = options.ztree_root_id;
        props.ztree_name_field = options.ztree_name_field;
        props.order = options.order;
        props.ztree_expend_level = options.ztree_expend_level;
        return props;
    },
};

registry.category("fields").add("ztree_select", fieldZTree);
// registry.category("fields").add("list.ztree_select", FieldZTree);
// registry.category("fields").add("kanban.ztree_select", FieldZTree);
