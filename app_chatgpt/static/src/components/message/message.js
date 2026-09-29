import {Message} from "@mail/core/common/message";
import {patch} from "@web/core/utils/patch";

// Odoo20: messageService 已移除，react 改为 Message 模型方法 message.react(content)；
// 复制文本功能 core 已提供 copyMessageText()，无需再 patch copy()

patch(Message.prototype, {
  async onClickMarkAsGood() {
    this.message.react('👍');
  },

  async onClickMarkAsBad() {
    this.message.react('👎');
  },
});
