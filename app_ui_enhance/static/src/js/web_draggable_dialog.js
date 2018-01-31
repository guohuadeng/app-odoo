odoo.define('app_ui_enhance.web_draggable_dialog', function (require) {
'use strict';

    var Dialog = require('web.Dialog');

    Dialog.include({
        open: function () {
            this._super.apply(this, arguments);
            this._opened.done(function(){
                $(".modal.in").draggable({
                    handle: ".modal-header"
                });
            });
            return this;
        },
    });
});
