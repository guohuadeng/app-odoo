/** @odoo-module **/

import { ListRenderer } from "@web/views/list/list_renderer";
import { patch } from "@web/core/utils/patch";

/**
 * 优化 one2many list 的空行填充策略：
 * - 原生 Odoo：至少保证 4 行显示（含 Add a line 行），即 0 条数据时有 3 个空行
 * - 优化后：仅当无数据时补充 1 个空行，有数据时不补充空行
 */
patch(ListRenderer.prototype, {
    get getEmptyRowIds() {
        // 仅当没有数据行时，补充 1 个空行；有数据时不补充
        let nbEmptyRow = this.props.list.records.length === 0 ? 1 : 0;
        return Array.from(Array(nbEmptyRow).keys());
    },
});
