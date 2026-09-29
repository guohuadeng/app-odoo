import { Message } from "@mail/core/common/message_model";
import { assignDefined } from "@mail/utils/common/misc";
import { patch } from "@web/core/utils/patch";

// 参考模块 whatsapp
// Odoo20: Message 模型 update(data, options) 由基类 Record 提供，
// is_ai 等自定义字段经后端 Store 下发；需透传 options 保持 forceApply 语义

patch(Message.prototype, {
    update(data, options) {
        assignDefined(this, data, ["human_prompt_tokens", "ai_completion_tokens", "is_ai"]);
        return super.update(data, options);
    },
});
