/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { Many2XAutocomplete } from "@web/views/fields/relational_utils";
import { Ztree } from "@app_web_widget_ztree/js/ztree";
import { sprintf } from "@web/core/utils/strings";

export class ZtreeMany2X extends Many2XAutocomplete {
    setup() {
        super.setup();
        let self = this;
        self.props = Object.assign(self.props, {
            setting: {
                callback: {
                    onClick: function (event, treeId, treeNode, clickFlag) {
                        self.onSelect(event, {
                            treeId: treeId,
                            treeNode: treeNode,
                        });
                    }
                }
            },
            data: Object.assign(self.props.data,{
                ztree_model: self.props.resModel,
            }),
        })
    };

    async loadOptionsSource(request) {
        //数据初始化
        if (this.lastProm) {
            this.lastProm.abort(false);
        }
        let ztree_Max = 1000;
        let data = this.props.data;
        var domain = data.ztree_domain;
        if (data.ztree_name_field && request && request.trim().length >= 1) {
            domain = domain.concat([[data.ztree_name_field, 'ilike', request]]);
        }

        let para = {
            context: data.ztree_context,
            domain: domain,
            parent_key: data.ztree_parent_key,
            root_id: data.ztree_root_id,
            expend_level: data.ztree_expend_level,
            name_field: data.ztree_name_field,
            order: data.order,
            limit: parseInt(data.limit ? data.limit : ztree_Max),
            type: data.ztree_type,
            //如果 type='chart'，要按 selected_id 得到 root_id 遍历
            selected_id: data.ztree_selected_id,
        }
        this.lastProm = this.orm.call(this.props.resModel, 'search_ztree', [], para)

        const records = await this.lastProm;
        const options = records;
        const max_id = Math.max.apply(Math,records.map(item => { return item.id }))

        if (this.props.quickCreate && request.length) {
            options.push({
                id: max_id + ztree_Max + 1,
                name: sprintf(_t(`Create "%s"`), request),
                label: sprintf(_t(`Create "%s"`), request),
                classList: "o_m2o_dropdown_option o_m2o_dropdown_option_create",
                font: {'text-align': 'right', 'padding-right': '10px'},
                action: async (params) => {
                    try {
                        await this.props.quickCreate(request, params);
                    } catch (e) {
                        if (e && e.name === "RPC_ERROR") {
                            const context = this.getCreationContext(request);
                            return this.openMany2X({ context });
                        }
                        // Compatibility with legacy code
                        if (e && e.message && e.message.name === "RPC_ERROR") {
                            // The event.preventDefault() is necessary because we still use the legacy
                            e.event.preventDefault();
                            const context = this.getCreationContext(request);
                            return this.openMany2X({ context });
                        }
                        throw e;
                    }
                },
            });
        }

        const canCreateEdit =
            "createEdit" in this.activeActions
                ? this.activeActions.createEdit
                : this.activeActions.create;

        if (request.length && canCreateEdit) {
            const context = this.getCreationContext(request);
            options.push({
                id: max_id + ztree_Max + 2,
                name: _t("Create and edit..."),
                label: _t("Create and edit..."),
                classList: "o_m2o_dropdown_option o_m2o_dropdown_option_create_edit",
                font: {'text-align': 'right', 'padding-right': '10px'},
                action: () => this.openMany2X({ context }),
            });
        }

        if (!this.props.noSearchMore && this.props.searchLimit < records.length) {
            options.push({
                id: max_id + ztree_Max + 3,
                name: _t("Search More..."),
                label: _t("Search More..."),
                classList: "o_m2o_dropdown_option o_m2o_dropdown_option_search_more",
                font: {'text-align': 'right', 'padding-right': '10px'},
                action: this.onSearchMore.bind(this, request),
            });
        }
        return options;
    }

    onSelect(option, params = {}) {
        let self = this;
        let record = {
            id: 0,
            name: '',
        };
        if (params.treeNode) {
            if (params.treeNode.action) {
                const autoCompleteInput = this.autoCompleteContainer.el.querySelector("input");
                return params.treeNode.action(autoCompleteInput);
            }
            else
                record = {
                    id: params.treeNode.id,
                    name: params.treeNode.name,
                };
        }
        self.props.data.ztree_selected_id = record.id;
        self.props.update([record], params);
        const autoCompleteInput = this.autoCompleteContainer.el.querySelector("input");
        autoCompleteInput.setAttribute('data-ztree_selected_id', record.id);
    }
}

ZtreeMany2X.template = "App.ZtreeMany2X";
ZtreeMany2X.components = { Ztree };
ZtreeMany2X.props = {
    ...Many2XAutocomplete.props,
    data: {type: Object, optional: true},
}