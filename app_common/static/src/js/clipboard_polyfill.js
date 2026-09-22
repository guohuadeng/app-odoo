/** @odoo-module **/

// 非安全上下文（http 且非 localhost 域名）下 navigator.clipboard 不存在，
// web_tour 的 tour_helpers_clipboard 模块加载时直接访问 writeText 会抛错，
// 连锁导致 @web_tour/tour_interactive/tour_interactive 无法启动。
// 此文件通过 manifest 的 before 指令插在核心 clipboard 文件之前执行。
if (!window.navigator.clipboard) {
    Object.defineProperty(window.navigator, "clipboard", {
        value: {
            writeText: () => Promise.resolve(),
            readText: () => Promise.reject(new Error("Clipboard API unavailable in insecure context")),
        },
        configurable: true,
    });
}
