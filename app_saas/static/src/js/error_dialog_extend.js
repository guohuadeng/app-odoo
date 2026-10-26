odoo.define('app_saas.error_dialog_extend', function (require) {
"use strict";

/**
 * v13 旧框架下扩展错误对话框，增加"申请支持"按钮：
 * 点击后打开 error.submit.wizard，由服务端提交报错信息。
 * 说明：v18 使用 OWL patch + 模板继承，v13 无 OWL，改为在 show_error
 * 生成的 Dialog 页脚追加按钮（页脚在 willStart 后才创建，须用 opened 回调）。
 */

var CrashManager = require('web.CrashManager');
var core = require('web.core');

var _t = core._t;

CrashManager.include({
    show_error: function (error) {
        var dialog = this._super.apply(this, arguments);
        if (!dialog) {
            return dialog;
        }
        var self = this;
        var $button = $('<button/>', {
            type: 'button',
            'class': 'btn btn-warning o_submit_error_button',
            title: _t('Report this error to OdooAi.cn for support Via Ai Passport'),
        })
        .append($('<i/>', {'class': 'fa fa-paper-plane mr4'}))
        .append(document.createTextNode(_t('Apply Support')));

        $button.on('click', function () {
            var traceback = (error && (error.traceback || (error.data && error.data.debug))) || '';
            var title = (error && error.type) || _t('Error');
            self.do_action({
                name: _t('Submit Error'),
                type: 'ir.actions.act_window',
                res_model: 'error.submit.wizard',
                view_mode: 'form',
                views: [[false, 'form']],
                target: 'new',
                context: {
                    default_issue_url: window.location.href,
                    default_issue_title: title,
                    default_issue_body: traceback,
                },
            });
        });

        dialog.opened(function () {
            if (dialog.$footer && dialog.$footer.length &&
                    !dialog.$footer.find('.o_submit_error_button').length) {
                dialog.$footer.append($button);
            }
        });
        return dialog;
    },
});

});
