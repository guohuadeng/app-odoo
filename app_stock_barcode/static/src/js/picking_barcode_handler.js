odoo.define('app_stock_barcode.appPickingBarcodeHandler', function (require) {
    "use strict";

    var core = require('web.core');
    var appFormViewBarcodeHandler = require('stock_barcode.PickingBarcodeHandler');

//用于获取最后扫码的产品，继承覆盖
    appFormViewBarcodeHandler.include({
        try_increasing_po_qty: function (barcode) {
            function is_suitable(pack_operation) {
                return pack_operation.get('product_barcode') === barcode
                    && !pack_operation.get('lots_visible')
                    && !pack_operation.get('location_processed')
                    && !pack_operation.get('result_package_id');
            }

            var po_field = this.form_view.fields.pack_operation_product_ids;
            var po_records = this._get_records(po_field);
            var candidate = this._get_candidates(po_records, is_suitable);
            if (candidate) {

                this.field_manager.set_values({'last_op_product': candidate.get('product_id')}).done(function () {
                    self.updating = false;
                });
                return po_field.data_update(candidate.get('id'), {'qty_done': candidate.get('qty_done') + 1}).then(function () {
                    return po_field.viewmanager.active_view.controller.reload_record(candidate);
                });
            } else {
                return $.Deferred().reject();
            }
        },
    });

});
