/** @odoo-module */

import { ExpenseDashboardListRenderer, ExpenseListController } from '@hr_expense/views/list';
import { registry } from '@web/core/registry';
import { listView } from "@web/views/list/list_view";

export class SuperbarDashboardListRenderer extends ExpenseDashboardListRenderer {
    static template = "app_hr_expense_superbar.DashboardListRenderer";
}

registry.category('views').add('hr_expense_dashboard_tree', {
    ...listView,
    buttonTemplate: 'hr_expense.ListButtons',
    Controller: ExpenseListController,
    Renderer: SuperbarDashboardListRenderer,
}, { force: true });
