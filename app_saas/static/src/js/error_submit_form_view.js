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
            let response;
            try {
                console.log("开始发送请求到:", errorReportUrl);
                console.log("请求数据:", submitData);
                response = await fetch(errorReportUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'User-Agent': 'OdooAppSaas-Client/18.0',
                    },
                    body: JSON.stringify(submitData),
                });
                console.log("收到响应:", response.status, response.statusText);
                console.log("响应头:", [...response.headers.entries()]);
            } catch (fetchError) {
                // 网络请求失败（CORS、DNS、连接失败等）
                console.error("Fetch 请求失败详情:", fetchError);
                console.error("Fetch 错误名称:", fetchError.name);
                console.error("Fetch 错误消息:", fetchError.message);
                throw new Error(_t("无法连接到服务器，请检查网络或联系管理员 (" + fetchError.message + ")"));
            }

            // 解析响应数据
            let resultData;
            try {
                const responseText = await response.text();
                console.log("响应内容:", responseText);
                resultData = responseText ? JSON.parse(responseText) : {};
            } catch (parseError) {
                console.error("解析响应失败:", parseError);
                resultData = {};
            }

            if (response.ok && resultData.success) {
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

                // 3秒后关闭向导
                setTimeout(() => {
                    this.env.services.action.doAction({ type: "ir.actions.act_window_close" });
                }, 3000);
            } else {
                // 处理服务器返回的错误
                const errorMessage = resultData.message || `HTTP ${response.status}: ${response.statusText}`;
                throw new Error(errorMessage);
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
