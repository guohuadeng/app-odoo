/** @odoo-module **/
import { Message } from "@mail/core/common/message_model";
import { assignDefined } from "@mail/utils/common/misc";
import { patch } from "@web/core/utils/patch";

// 参考模块 whatsapp

patch(Message.prototype, {
    update(data) {
        assignDefined(this, data, ["human_prompt_tokens", "ai_completion_tokens", "is_ai"]);
        super.update(data);
    },
});

//
// registerPatch({
//     name: 'Message',
//     modelMethods: {
//         convertData(data) {
//             const data2 = this._super(data);
//             if ('human_prompt_tokens' in data) {
//                 data2.human_prompt_tokens = data.human_prompt_tokens;
//             }
//             if ('ai_completion_tokens' in data) {
//                 data2.ai_completion_tokens = data.ai_completion_tokens;
//             }
//             if ('is_ai' in data) {
//                 data2.is_ai = data.is_ai;
//             }
//             return data2;
//         },
//     },
//     fields: {
//         human_prompt_tokens: attr(),
//         ai_completion_tokens: attr(),
//         is_ai: attr(),
//
//     }
// })