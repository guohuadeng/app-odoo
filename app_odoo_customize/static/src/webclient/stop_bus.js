/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { MultiTabSharedWorkerPlugin } from "@bus/multi_tab_shared_worker_plugin";
import { BusPlugin } from "@bus/services/bus_plugin";

// app_stop_subscribe 为 True 时，除停用邮件订阅外，还彻底停用 bus：
// 不创建 SharedWorker、不建立 websocket、不订阅频道，因此不再有实时推送、
// presence 在线状态检测和断线重连。Windows 下 Odoo 以 workers=0 运行，
// 每个页签的 websocket 都会长期占用一个请求线程，断开后还会反复重连，
// 关闭它可明显提速本地后台。
// 与 Python 侧 models/mail_thread.py 的判定保持一致：仅当值为 "True" 时停用；
// "False"、空值或其他值一律不 patch，保持原生 bus 行为。
const appStopSubscribe = session.app_stop_subscribe === "True";

if (appStopSubscribe) {
    patch(BusPlugin.prototype, {
        async ensureWorkerStarted() {},
        async addChannel() {},
        deleteChannel() {},
        async start() {},
        stop() {},
        async forceUpdateChannels() {},
        async send() {},
        setLoggingEnabled() {},
        downloadLogs() {},
        subscribe() {
            return () => {};
        },
        unsubscribe() {},
    });
    // 多页签选举依赖 bus worker；bus 已停用时直接视为主页签，
    // 避免通知相关代码 await 一个永远不会返回的 worker 消息。
    patch(MultiTabSharedWorkerPlugin.prototype, {
        async isOnMainTab() {
            return true;
        },
    });
    console.info("app_odoo_customize: app_stop_subscribe is on, websocket bus disabled.");
}
