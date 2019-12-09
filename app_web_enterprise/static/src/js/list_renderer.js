odoo.define('app_web_enterprise.ListRenderer', function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');

    ListRenderer.include({
        _renderBody: function () {
            var self = this;
            var $rows = this._renderRows();
            while ($rows.length < 1) {
                $rows.push(self._renderEmptyRow());
            }
            return $('<tbody>').append($rows);
        },
    });

    return ListRenderer;
});
