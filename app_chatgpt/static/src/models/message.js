/** @odoo-module **/

import { insert } from '@mail/model/model_field_command';
import { attr, many, one } from '@mail/model/model_field';
import { registerPatch } from '@mail/model/model_core';

registerPatch({
    name: 'Message',
    modelMethods: {
        convertData(data) {
            const data2 = this._super(data);
            if ('human_prompt_tokens' in data) {
                data2.human_prompt_tokens = data.human_prompt_tokens;
            }
            if ('ai_completion_tokens' in data) {
                data2.ai_completion_tokens = data.ai_completion_tokens;
            }
            if ('is_ai' in data) {
                data2.is_ai = data.is_ai;
            }
            return data2;
        },
    },
    fields: {
        human_prompt_tokens: attr(),
        ai_completion_tokens: attr(),
        is_ai: attr(),

    }
})