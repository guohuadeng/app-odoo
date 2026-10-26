odoo.define('app_saas.error_submit_form_view', function (require) {
"use strict";

/**
 * v13 报错提交向导：拦截"提交"按钮，改为调用服务端提交方法，
 * 按返回结果显示通知并在成功后关闭向导（v18 为 OWL 版 FormController，v13 用旧框架）。
 */

var FormController = require('web.FormController');
var FormView = require('web.FormView');
var viewRegistry = require('web.view_registry');
var core = require('web.core');

var _t = core._t;

var ErrorSubmitFormController = FormController.extend({
    /**
     * @override
     */
    _callButtonAction: function (attrs, record) {
        if (attrs.name === 'action_submit_error') {
            return this._submitError(record || this.model.get(this.handle));
        }
        return this._super.apply(this, arguments);
    },

    _submitError: function (record) {
        var self = this;
        this.displayNotification({
            title: _t('Submitting'),
            message: _t('Submitting the error report...'),
            type: 'info',
        });
        return this._rpc({
            model: 'error.submit.wizard',
            method: 'action_submit_error',
            args: [[record.res_id]],
        }).then(function (result) {
            result = result || {};
            var params = result.params || {};
            self.displayNotification({
                title: params.title || '',
                message: params.message || result.message || '',
                type: params.type || (result.success ? 'success' : 'danger'),
                sticky: !result.success,
            });
            if (result.success) {
                self.trigger_up('close_dialog');
            }
        });
    },
});

var ErrorSubmitFormView = FormView.extend({
    config: _.extend({}, FormView.prototype.config, {
        Controller: ErrorSubmitFormController,
    }),
});

viewRegistry.add('error_submit_form', ErrorSubmitFormView);

});
