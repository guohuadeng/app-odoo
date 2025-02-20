/** @odoo-module */

import {X2ManyField, x2ManyField} from '@web/views/fields/x2many/x2many_field';

import { onMounted, useRef } from "@odoo/owl";
import {session} from "@web/session";
import {Ztree} from './ztree';
import {ZtreeMany2X} from './ztree_many2x';
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {_lt} from "@web/core/l10n/translation";
import {FieldZTree} from "./ztree_select";

export class FieldZTreeChart extends X2ManyField {
  async setup() {
    super.setup();
    let self = this;
    let setting = self.props.setting;
    let data = self.props;
    this.rpc = useService("rpc");
    this.orm = useService("orm");
    this.action = useService("action");
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
      callback: {
        onClick: function (event, treeId, treeNode, clickFlag) {
          self.onSelect(event, {
            treeId: treeId,
            treeNode: treeNode,
          });
        }
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

    if (self.props && self.props.zNodes && self.props.zNodes.length)
      this.zNodes = self.props.zNodes;
    this.ztree_field = self.props.name;
    this.ztree_model = self.props.record.resModel;
    this.ztree_parent_key = self.field.relation_field;
    //todo: root_id，这个是节点的根id，用 parent_left < x < parent_right 实现，在 domain 增加值
    this.ztree_root_id = data.ztree_root_id;
    this.ztree_domain = data.ztree_domain;
    this.ztree_context = data.ztree_context ? data.ztree_context : session.user_context;
    this.order = data.order;
    this.ztree_selected_id = Number(data.record.data.id);
    this.ztree_selected_vals = [];
    this.ztree_with_sub_node = data.ztree_with_sub_node;
    this.ztree_index = data.ztree_index;
    this.ztree_add_show_all = false;
    //默认2级
    this.ztree_expend_level = data.ztree_expend_level ? data.ztree_expend_level : 2;
    this.ztree_name_field = data.ztree_name_field;
    this.limit = data.limit > 0 ? data.limit : ztree_Max;
    self.ztree_id = 'ztree-' + self.guid();
    this.ztree_type = data.ztree_type ? data.ztree_type : 'chart';
    onMounted(this.handleComponentUpdate.bind(this));
  }

  async handleComponentUpdate() {
      let self = this;
      self.zNodes = await self.loadZchartSource().then(function (){
          var $el = $('#' + self.ztree_id);
          if ($el && self.zNodes)    {
              self.$Ztree = $.fn.zTree.init($el, self.setting, self.zNodes);
              let ztree_selected_id = self.props.record.data.id;
              if (ztree_selected_id != undefined && ztree_selected_id > 0 && self.props.record.data.id) {
                  var node = self.$Ztree.getNodeByParam('id', ztree_selected_id, null);
                  if (node)
                      self.$Ztree.selectNode(node);
              };
          };
      });
  }

  async loadZchartSource() {
    //数据初始化
    let self = this;
    if (self.lastProm) {
      self.lastProm.abort(false);
    }
    let ztree_Max = 1000;
    var domain = self.ztree_domain || [];
    let root_id = self.ztree_root_id;
    if (!root_id) {
      root_id = self.props.record.data.parent_id ? self.props.record.data.parent_id[0] : 0;
    }
    if (!root_id) {
      root_id = self.props.record.data.id;
    }
    self.ztree_selected_id = self.props.record.data.id;
    let para = {
      context: self.ztree_context || {},
      domain: domain,
      parent_key: self.ztree_parent_key,
      root_id: root_id,
      expend_level: self.ztree_expend_level,
      name_field: self.ztree_name_field,
      order: self.order,
      limit: parseInt(self.props.limit ? self.props.limit : ztree_Max),
      type: 'chart',
      //如果 type='chart'，要按 selected_id 得到 root_id 遍历
      selected_id: self.ztree_selected_id,
    };
    this.lastProm = this.orm.call(this.props.record.resModel, 'search_ztree', [], para);

    const records = await this.lastProm;
    self.zNodes = records || [];
    return records;
  }

  async onSelect(option, params = {}) {
    var self = this;
    var record = {
      id: 0,
      name: '',
    };
    if (params.treeNode) {
        record = {
          id: params.treeNode.id,
            name: params.treeNode.name,
        };
        //todo: 面包屑处理不生效，后续优化
        // let action = await self.orm.call(self.props.record.resModel, 'get_formview_action', [record.id]);
        var action = self.env.model.action.currentController.action;
        action = {...action,
            res_id: record.id,
            views: [[false, "form"]],
        };
        var bs = self.env.config.breadcrumbs;
        if (bs.length > 1) {
            self.action.doAction(action, {
                clearBreadcrumbs: true,
            });
        } else {
            self.action.doAction(action);
        }
    }
  }

  guid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

}

FieldZTreeChart.components = {Ztree};

FieldZTree.components = {
    ...X2ManyField.components,
    Ztree,
    ZtreeMany2X,
};

FieldZTreeChart.props = {
  ...X2ManyField.props,
  ztree_parent_key: {type: String, optional: true},
  ztree_root_id: {type: Number, optional: true},
  ztree_name_field: {type: String, optional: true},
  order: {type: String, optional: true},
  ztree_expend_level: {type: String, optional: true},
};
FieldZTreeChart.supportedTypes = ["one2many"];
FieldZTreeChart.displayName = _lt("Hierarchy Chart");
FieldZTreeChart.template = 'App.FieldZtreeChart';

export const fieldZTreeChart = {
    ...x2ManyField,
    component: FieldZTreeChart,
    extractProps({ options }) {
        const props = x2ManyField.extractProps(...arguments);
        props.ztree_parent_key = options.ztree_parent_key;
        props.ztree_root_id = options.ztree_root_id;
        props.ztree_name_field = options.ztree_name_field;
        props.order = options.order;
        props.ztree_expend_level = options.ztree_expend_level;
        return props;
    },
};

registry.category("fields").add("ztree_chart", fieldZTreeChart);
