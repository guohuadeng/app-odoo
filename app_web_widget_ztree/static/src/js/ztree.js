/** @odoo-module */

import { AutoComplete } from "@web/core/autocomplete/autocomplete";
import { loadJS } from "@web/core/assets";
const { Component, useRef } = owl;
import {session} from "@web/session";
import { useService } from "@web/core/utils/hooks";
//todo: ztree 继承 import { AutoComplete } from "@web/core/autocomplete/autocomplete";
//field ztree 继承 fieldm2o，优化 xml 并入  Many2XAutocomplete
export class Ztree extends AutoComplete {
    setup() {
        super.setup();
        let self = this;
        let setting = self.props.setting;
        let data = self.props.data;
        this.rpc = useService("rpc");
        this.orm = useService("orm");
        this.ztree_root = useRef("ztree_root");
        this.$Ztree = false;
        this.zNodes = false;
        let ztree_Max = 1000;
        this.setting = {
            view: {
                selectedMulti: true,
                fontCss: function getFont(treeId, node) {
                    return node.font ? node.font : {};
                },
                nameIsHTML: true,
                showIcon: false,
                txtSelectedEnable: true,
            },
            data: {
                key: {
                    title: "title"
                },
                simpleData: {
                    enable: true,
                }
            }
        };

        if (setting)
            $.extend(this.setting, setting);

        //如果有定义zNodes，则直接按 zNodes数据展现，否则 rpc 取

        if (data && data.zNodes && data.zNodes.length)
            this.zNodes = data.zNodes;
        this.ztree_field = data.ztree_field;
        this.ztree_model = data.ztree_model;
        this.ztree_parent_key = data.ztree_parent_key;
        //todo: root_id，这个是节点的根id，用 parent_left < x < parent_right 实现，在 domain 增加值
        this.ztree_root_id = data.ztree_root_id;
        this.ztree_domain = data.ztree_domain;
        this.ztree_context = data.ztree_context ? data.ztree_context : session.user_context;
        this.order = data.order;
        this.ztree_selected_id = Number(data.ztree_selected_id);
        this.ztree_selected_vals = [];
        this.ztree_with_sub_node = data.ztree_with_sub_node;
        this.ztree_index = data.ztree_index;
        this.ztree_add_show_all = data.ztree_add_show_all;
        //默认2级
        this.ztree_expend_level = data.ztree_expend_level ? data.ztree_expend_level : 2;
        this.ztree_name_field = data.ztree_name_field;
        this.limit = data.limit > 0 ? data.limit : ztree_Max;
        this.ztree_id = 'ztree-' + this.guid();
        this.ztree_type = data.ztree_type ? data.ztree_type : 'select';

        //点击外部关闭ztree
        $(document).delegate('body', 'click', function (ev) {
            var $parent = $(ev.target).parents('.dropdown')
            if (!$parent.length && self.zNodes) {
                self.close()}
        });
    }

    loadSources(useInput) {
        let self = this;
        this.sources = [];
        this.state.activeSourceOption = null;
        const proms = [];
        let request = useInput ? this.inputRef.el.value.trim() : ""
        for (const pSource of this.props.sources) {
            const source = this.makeSource(pSource);
            this.sources.push(source);
            const options = this.loadOptions(
                pSource.options,
                useInput ? this.inputRef.el.value.trim() : ""
            );
            if (options instanceof Promise) {
                source.isLoading = true;
                const prom = options.then((options) => {
                    source.options = options.map((option) => this.makeOption(option));
                    source.isLoading = false;
                    this.state.optionsRev++;
                    this.zNodes = options;
                    this.state.open = true;
                });
                proms.push(prom);
            }
        }

        Promise.all(proms).then(() => {
            self.navigate(0);
            var $el = $('#' + self.ztree_id);
            if ($el) {
                self.$Ztree = $.fn.zTree.init($el, self.setting, self.zNodes);
                let ztree_selected_id = this.inputRef.el.getAttribute('data-ztree_selected_id');
                if (!request && ztree_selected_id != undefined && ztree_selected_id > 0) {
                    var node = self.$Ztree.getNodeByParam('id', ztree_selected_id, null);
                    if (node)
                        self.$Ztree.selectNode(node);
                }
            }
        });
    }

    makeOption(option) {
        let res = {};
        if (!option.action)
            option = {label: option.name, value: option.id};
        else
            option = {
                label: option.label,
                value: option.id,
                action: option.action
            }
        res = Object.assign(Object.create(option), {
            id: ++this.nextOptionId,
        });
        return res;
    }

    close() {
        super.close();
        if (this.zNodes) {
            $.fn.zTree.destroy(this.ztree_id);
            this.$Ztree = undefined;
            this.zNodes = false;
        }
    }

    onInputBlur() {
        const value = this.inputRef.el.value;
        if (
            this.props.autoSelect &&
            value.length > 0
        ) {
            ;
        } else {
            this.props.onBlur({
                inputValue: value,
            });
            this.close();
        }
    }

    guid() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    getChildNodes(treeNode) {
        var childNodes = this.$Ztree.transformToArray(treeNode);
        var nodes = new Array();
        var i;
        for (i = 0; i < childNodes.length; i++) {
            nodes[i] = childNodes[i].id;
        }

        return nodes.join(",");
    }
}

Ztree.template = "App.Ztree";

Ztree.props = {
    ...AutoComplete.props,
    setting: {type: Object, optional: true},
    data: {type: Object, optional: true},
};

Ztree.defaultProps = {
    ...AutoComplete.defaultProps,
};

