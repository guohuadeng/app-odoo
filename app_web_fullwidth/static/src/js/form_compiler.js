/** @odoo-module **/

/**
 * 表单全宽 + 沟通（Chatter）位置可配置。
 *
 * v20 迁移说明（本文件按 v20 原生扩展点重写，v18 的字符串替换写法已全部失效）：
 *
 * 1) 沟通位置：v18 是去改 FormCompiler 编译产物里 `t-attf-class` 的那串模板表达式
 *    （v18 mail/static/src/chatter/web/form_compiler.js 生成
 *     `{{ __comp__.uiService.size >= 6 ? "o-aside" : "mt-4 mt-md-0" }}`）。
 *    v20 把这套判断抽成了 FormRenderer 的 `mailLayout(hasAttachmentContainer)` 方法
 *    （mail/static/src/chatter/web/form_renderer.js:49），返回值决定
 *    「沟通在侧栏还是在下方」（mail/static/src/chatter/web/form_compiler.js:101-109）。
 *    官方自己就是用 `patch(FormRenderer.prototype, { mailLayout })` 扩展的，
 *    所以这里直接改返回值，不再做脆弱的字符串替换。
 *
 * 2) 表单主体伸缩方向：v18/v20 的 FormCompiler.compileForm 都会生成
 *    `d-flex d-print-block {{ __comp__.uiService.size < ${SIZES.XXL} ? "flex-column" : "flex-nowrap h-100" }}`
 *    （v20 web/static/src/views/form/form_compiler.js:224）。
 *    ⚠ v20 的 SIZES 枚举被精简过：v18 是 {XS:0, VSM:1, SM:2, MD:3, LG:4, XL:5, XXL:6}，
 *      v20 是 {XS:0, SM:1, MD:2, LG:3, XL:4, XXL:5}（@web/core/ui/ui_utils:3）
 *      ⇒ 原来硬编码的 `< 6` 字面量不再等于 `${SIZES.XXL}`，照抄 v18 会静默失配。
 *    这里改成用正则匹配 `__comp__.uiService.size < N`，N 取自 SIZES，跟版本走。
 */

import { FormCompiler } from "@web/views/form/form_compiler";
import { FormRenderer } from "@web/views/form/form_renderer";
import { SIZES } from "@web/core/ui/ui_utils";
import { patch } from "@web/core/utils/patch";

const chChatter = () => odoo.web_chatter_position;

// 主体的伸缩方向表达式（见上）。用正则而不是字面量，SIZES 变了也不会失配。
const FLEX_RE = /\{\{\s*__comp__\.uiService\.size\s*<\s*\d+\s*\?\s*"flex-column"\s*:\s*"flex-nowrap h-100"\s*\}\}/;

function setFlexDirection(el, mode) {
    const classes = el.getAttribute("t-attf-class");
    if (!classes) {
        return false;
    }
    const forced = mode === "sided" ? "flex-nowrap h-100" : "flex-column";
    const replaced = classes.replace(FLEX_RE, forced);
    if (replaced === classes) {
        return false;
    }
    el.setAttribute("t-attf-class", replaced);
    return true;
}

patch(FormRenderer.prototype, {
    /**
     * v20 原生钩子（mail/chatter/web/form_renderer.js:49）：
     * 返回值决定沟通区落在侧栏还是下方，以及附件预览与沟通的组合方式。
     * 这里按用户/全局配置强制走对应布局，其余情形交回原生判断。
     */
    mailLayout(hasAttachmentContainer) {
        const mode = chChatter();
        const native = super.mailLayout(hasAttachmentContainer);
        if (mode === "sided" && native === "BOTTOM_CHATTER") {
            return "SIDE_CHATTER";
        }
        if (mode === "bottom" && native === "SIDE_CHATTER") {
            return "BOTTOM_CHATTER";
        }
        return native;
    },
});

patch(FormCompiler.prototype, {
    compileForm(el, params) {
        const res = super.compileForm(el, params);
        const mode = chChatter();
        if (mode !== "sided" && mode !== "bottom") {
            return res; // "auto"：保持 v20 原生的响应式行为
        }
        setFlexDirection(res, mode);

        if (mode === "bottom") {
            // 下方模式还需要放开表单主体的宽度限制（SCSS 侧见 app_style_after.scss）
            const sheetBg = res.getElementsByClassName("o_form_sheet_bg")[0];
            if (sheetBg) {
                sheetBg.classList.add("customBottom");
                const chatter = sheetBg.parentElement?.querySelector(".o-mail-Form-chatter");
                chatter?.classList.add("customBottom");
            }
        }
        return res;
    },
});
