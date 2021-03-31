odoo.define('app_odoo_customize.dialog', function (require) {
'use strict';

    var Dialog = require('web.Dialog');

    Dialog.include({
        open: function () {
            this._super.apply(this, arguments);
            this._opened.then(function(){
                $(".modal-content").draggable({
                    handle: ".modal-header"
                });
            });
            return this;
        },
    });
});
