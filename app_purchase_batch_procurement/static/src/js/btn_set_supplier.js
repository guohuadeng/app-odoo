odoo.define('app_purchase_batch_procurement.btn_set_supplier', function (require) {
    "use strict";

    var core = require('web.core');
    var ListView = require('web.ListView');
    var web_client = require('web.web_client')
    var QWeb = core.qweb;

    ListView.include({

        render_buttons: function ($node) {
            if ($node) {
                var self = this;
                this._super($node);
                this.$buttons.find('.o_list_btn_set_supplier').click(this.proxy('set_supplier_action'));
                this.$buttons.find('.o_list_btn_batch_procurement').click(this.proxy('batch_procurement_action'));
            }
        },
        set_supplier_action: function () {
            //纯js取
            // var active_ids = $.map($('.o_list_view .o_list_record_selector :checkbox:checked'), function (el) {
            //     return $(el).closest('tr').data('id');
            // });
            //odoo内置方法取值
            var active_ids = this.groups.get_selection().ids
            this.do_action({
                type: "ir.actions.act_window",
                name: " Set Supplier",
                res_model: "product.set.supplier.wiz",
                views: [[false, 'form']],
                view_type: 'form',
                view_mode: 'form',
                multi: 1,
                key2: "client_action_multi",
                src_model: "procurement.order",
                active_model: "procurement.order",
                target: 'new',
                context: {'active_ids': active_ids}
            });
            return {'type': 'ir.actions.client'}
        },
        batch_procurement_action: function () {
            // var active_ids = self.$.map($('.o_list_view .o_list_record_selector :checkbox:checked'), function (el) {
            //     return $(el).closest('tr').data('id');
            // });
            var active_ids = this.groups.get_selection().ids
            // var active_ids = self.getSelection().ids;
            this.do_action({
                type: "ir.actions.act_window",
                name: "Request Procurements",
                res_model: "procurement.batch.generator",
                views: [[false, 'form']],
                view_type: 'form',
                view_mode: 'form',
                multi: 1,
                key2: "client_action_multi",
                src_model: "product.product",
                active_model: "product.product",
                target: 'new',
                context: {'active_ids': active_ids}
            });
            return {'type': 'ir.actions.client'}
        }
    });

});