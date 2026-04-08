/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

class ErrorSubmitFormController extends FormController {
    setup() {
        super.setup();
        this.notification = useService("notification");
        this.orm = useService("orm");
    }

    /**
     * 重写保存方法，拦截action_submit_error按钮的点击
     */
    async beforeExecuteActionButton(clickParams) {
        // 如果是提交错误按钮，使用JS直接提交
        if (clickParams.name === "action_submit_error") {
            await this._submitErrorViaJs();
            return false; // 阻止继续执行Python方法
        }
        return super.beforeExecuteActionButton(...arguments);
    }

    /**
     * 使用JS直接提交错误报告
     */
    async _submitErrorViaJs() {
        const record = this.model.root;

        // 获取表单数据
        const submitData = {
            issue_url: record.data.issue_url || 'http://localhost',
            issue_title: record.data.issue_title || 'Odoo错误报告',
            issue_body: record.data.issue_body || '',
            dbuuid: record.data.dbuuid || '',
            submit_login: record.data.submit_login || '',
            submit_type: record.data.submit_type || 'ticket',
            odoo_version: record.data.odoo_version || '',
            timestamp: new Date().toISOString(),
        };

        // 获取用户信息
        const user = this.env.services.user;
        if (user) {
            submitData.user_name = user.name || '';
            submitData.user_email = user.email || '';
        }

        const errorReportUrl = record.data.error_report_url || 'https://www.odooai.cn/service/error-report';

        try {
            // 显示提交中状态
            this.notification.add(_t("正在提交错误报告..."), {
                type: "info",
                sticky: false,
            });

            // 发送HTTP请求
            const response = await fetch(errorReportUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'User-Agent': 'OdooAppSaas-Client/18.0',
                },
                body: JSON.stringify(submitData),
            });

            if (response.ok) {
                const resultData = await response.json().catch(() => ({}));
                const ticketId = resultData.ticket_id || 'N/A';

                // 显示成功通知
                this.notification.add(
                    _t("错误报告已提交到 odooai.cn，工单号: %s。我们会尽快处理！", ticketId),
                    {
                        type: "success",
                        sticky: false,
                        title: _t("提交成功"),
                    }
                );

                // 关闭向导
                this.env.services.action.doAction({ type: "ir.actions.act_window_close" });
            } else {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
        } catch (error) {
            console.error("提交错误报告失败:", error);

            // 显示失败通知
            this.notification.add(
                _t("提交失败: %s。请检查网络连接后重试。", error.message),
                {
                    type: "danger",
                    sticky: true,
                    title: _t("提交失败"),
                }
            );
        }
    }
}

/**
 * 注册自定义视图
 */
export const errorSubmitFormView = {
    ...formView,
    Controller: ErrorSubmitFormController,
};

registry.category("views").add("error_submit_form", errorSubmitFormView);
