/** @odoo-module **/

import { insert } from '@mail/model/model_field_command';
import { getBundle, loadBundle } from '@web/core/assets';
import { registerPatch } from '@mail/model/model_core';

registerPatch({
        name: 'EmojiRegistry',
        recordMethods: {
            async loadEmojiData() {
                this.update({isLoading: true});
                await getBundle('mail.assets_model_data').then(loadBundle);
                //优化 data 文件
                const {emojiCategoriesData, emojisData} = await odoo.runtimeImport("@app_chatgpt/models_data/emoji_data");
                if (!this.exists()) {
                    return;
                }
                this._populateFromEmojiData(emojiCategoriesData, emojisData);
            },
            async _populateFromEmojiData(dataCategories, dataEmojis) {
                dataCategories.map(category => {
                    const emojiCount = dataEmojis.reduce((acc, emoji) => emoji.category === category.name ? acc + 1 : acc, 0);
                    this.update({
                        dataCategories: insert({
                            name: category.name,
                            displayName: category.displayName,
                            title: category.title,
                            sortId: category.sortId,
                            emojiCount,
                        }),
                    });
                });
                this.models['Emoji'].insert(dataEmojis.map(emojiData => ({
                    codepoints: emojiData.codepoints,
                    shortcodes: emojiData.shortcodes,
                    emoticons: emojiData.emoticons,
                    name: emojiData.name,
                    keywords: emojiData.keywords,
                    emojiDataCategory: {name: emojiData.category},
                })));
                this.update({
                    isLoaded: true,
                    isLoading: false,
                });
            },
        },
    }
)
