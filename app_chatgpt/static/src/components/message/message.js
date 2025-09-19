/** @odoo-module */
import {Message} from "@mail/core/common/message";
import {patch} from "@web/core/utils/patch";

patch(Message.prototype, {
  async copy() {
    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(this.message.body.replaceAll('<br>', '\n').replaceAll('</br>', '\n'), "text/html");
    const textInputContent = htmlDoc.body.textContent;
    const tempInput = document.createElement("textarea");
    tempInput.value = textInputContent;
    document.body.appendChild(tempInput);
    tempInput.select();
    tempInput.setSelectionRange(0, tempInput.value.length);
    document.execCommand("copy");
    document.body.removeChild(tempInput);
  },
  async onClickMarkAsGood() {
    this.messageService.react(this.message, '👍');
  },

  async onClickMarkAsBad() {
    this.messageService.react(this.message, '👎');
  },
});
