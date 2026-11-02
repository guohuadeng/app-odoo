# app-odoo Modules (Odoo 20)

> Odoo 20 modules from odooai.cn — **55** modules in total.
> Each module directory contains `__manifest__.py` and `static/description/` (index.html, index_cn.html, banner.png, banner_cn.png and other assets).

## Structure

```
app-odoo/
  app_xxx/
    __manifest__.py
    models/ views/ data/ security/
    static/description/   # App Store description pages, banners and screenshots
```

## Module List

Modules are grouped by Odoo category. Descriptions come from each module `summary` in `__manifest__.py`.

### Sales

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_sale_product_multi_add` | Sale Order Product Multi Batch Add | One click batch add products to sale order with filter, group and detail form. | 20.0.24.12.03 |

### Inventory

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_purchase_product_multi_add` | Purchase Order Product Multi Batch Add | One click batch add products to purchase order with filter, group and detail form. | 20.0.24.12.03 |
| `app_stock_picking_product_multi_add` | Stock Picking Order Product Multi Batch Add | One-click to add multi products to stock picking order | 20.0.24.12.03 |
| `app_stock_superbar` | Stock Superbar zTree Navigator | Stock location tree navigator for picking, batch, move and lot | 20.0.25.09.08 |
| `app_stock_superbar_pro` | Stock Superbar Pro with Date Search | Advance stock search with date range and parent children tree | 20.0.25.09.08 |

### Accounting

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_account_invoice_product_multi_add` | Account Invoice Product Multi Add | One Click to batch add multiple products to Customer Invoice and Vendor Bill with filter and group. | 20.0.24.12.03 |
| `app_account_superbar` | Account Superbar Navigator | Browse journal by account chart with parent-children tree navigator for list, kanban, pivot, graph view. | 20.0.26.08.21 |
| `app_account_ztree` | Account Multi Level Chart Tree | Multi Level Account Chart tree with parent-children zTree widget for list select navigator. | 20.0.26.10.08 |
| `l10n_cn_standard_latest` | Latest Chinese Accounting Chart | Latest Chinese accounting chart (general and small-scale taxpayer) with multi-level account support | 20.0.26.10.28 |

### Human Resources

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_hr_expense_superbar` | Hr Expense Superbar | Browse hr expense by departments or Analytic Account. Easy to navigator and browse any data. Support list, kanban, pivot, graph view. ztree widget. hr… | 20.0.26.05.20 |
| `app_hr_expense_superbar_pro` | Hr Expense Superbar Pro | Browse hr expense by departments or Analytic Account. Easy to navigator and browse any data. Support list, kanban, pivot, graph view. ztree widget. hr… | 20.0.26.10.23 |
| `app_hr_superbar` | Employee Navigator by Department | Browse employees by department tree with Superbar advance search and organization chart. | 20.0.24.11.12 |

### Website

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_ai_bard` | 谷歌Gemini AI支持 | Google Gemini AI integration for Odoo AI Center with multi-robot chat and training. | 20.0.26.10.21 |
| `app_chatgpt` | AI服务中心聚合全网AI | Multi AI integration with ChatGPT4, DeepSeek, Ali Qwen, Baidu in Odoo AI Center. | 20.0.26.10.12 |
| `app_claude` | Claude AI for Odoo AI Center | Claude AI for Odoo AI Center. Ai Aigc Center including Claude, Deepseek, Azure Chatgpt Ai, OpenAi Chatgpt Ai. Integration All Ai robot Api, like Anthr… | 20.0.26.10.12 |
| `app_deepseek` | Deepseek AI for Odoo AI Center | Deepseek AI for Odoo AI Center. Ai Aigc Center including Deepseek, Azure Chatgpt Ai, OpenAi Chatgpt Ai. Integration All Ai robot Api, like Azure OpenA… | 20.0.26.10.12 |
| `app_website_blog_editor` | Website Blog & Page Source Code Editor | Edit website page and blog in source code mode with mass edit and SEO | 20.0.26.10.21 |
| `app_website_blog_superbar` | Website Blog Search Enhance Superbar | Enhanced blog search with tree navigation for browsing posts | 20.0.24.11.12 |
| `app_website_sale_editor` | Website Product SEO & Source Code Editor | Edit e-commerce product page in source code mode with mass SEO | 20.0.26.10.14 |

### Point of Sale

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_pos_superbar` | POS Order Navigator by Store | Browse POS orders by store, salesperson and status with Superbar. | 20.0.25.06.10 |

### Technical

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_odoo_sync` | 实例数据同步（Odoo 18 → 20） | Pull partners and users from a remote Odoo 18 instance with read-only RPC. | 20.0.26.10.31 |

### Extra Tools

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_odoo_customize` | Odoo20 Tweak OEM Development Enhance.Boost | 60+ Odoo Enhance in 1 click Tweak odoo. Change Odoo to your OEM brand.all in one odoo enhancement. for Customize,UI,Boost Security,Development. ChatWi… | 20.0.26.10.29 |

### Extra tools

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_auto_backup` | Database Auto Backup and Download | Automated database backup with SFTP remote backup, manual one-click backup and easy download. | 20.0.26.09.20 |
| `app_base_company_zchart` | Group Company Multi Level Chart Hierarchy | Multi level company hierarchy chart with zChart widget for parent-children relation. | 20.0.25.06.10 |
| `app_base_superbar` | Easy Admin Navigator with Superbar | Quick admin navigator for menu, views, fields, actions, users with Superbar tree. | 20.0.26.09.15 |
| `app_common` | odooAi Common Util and Tools | Core module for odooai.cn apps with common utilities and tools. | 20.0.26.10.13 |
| `app_contacts_superbar` | Contacts Partner Superbar | Browse contacts by company, category and industry with hierarchical tree navigator | 20.0.26.10.15 |
| `app_contacts_superbar_pro` | Contacts Superbar Pro | Enhanced contacts navigator with company type and date range search | 20.0.24.12.04 |
| `app_crm_superbar` | CRM Superbar | Navigate CRM leads and opportunities by stage, team and campaign | 20.0.24.11.12 |
| `app_event_superbar` | Event Advance Search Superbar | Browse events by stage and tag category with Superbar tree navigator. | 20.0.25.06.10 |
| `app_event_superbar_pro` | Event Advance Search Browse by Stage and Date | Browse event by stage and date with Superbar advance search sidebar. | 20.0.26.10.25 |
| `app_hr_ztree` | HR Department zTree Widget | HR department and employee parent children tree selector with zTree widget. | 20.0.24.12.09 |
| `app_mail_superbar` | Mail Quick Navigator | Browse and search all mail by category with Superbar advance search. | 20.0.24.11.12 |
| `app_module_superbar` | Apps Navigator by Category | Browse apps by category tree and module navigator with Superbar. | 20.0.24.11.12 |
| `app_mrp_superbar` | MRP Manufacturing Orders Navigator | Browse manufacturing orders by materials availability and work center with Superbar. | 20.0.25.06.10 |
| `app_product_category_zchart` | Category zChart Hierarchy | Product category multi level hierarchy chart widget with N+1/N+2 support. | 20.0.25.02.27 |
| `app_product_superbar` | Product Browse by Category Navigator | Browse products by category tree with Superbar advance search. | 20.0.26.09.09 |
| `app_product_superbar_pro` | Product Browse by Category Navigator Pro | Product category advance search Pro version with enhanced features. | 20.0.25.04.19 |
| `app_product_ztree` | Product Category zTree Widget | Product category parent children tree selector with zTree widget. | 20.0.24.12.09 |
| `app_project_superbar` | Project & Task Navigator | Browse projects by company, partner, user and stage with Superbar. | 20.0.26.08.18 |
| `app_purchase_superbar` | Purchase Superbar Navigator | Browse purchase orders by vendor with tree navigator across list, kanban, pivot and graph views. | 20.0.26.08.19 |
| `app_purchase_superbar_pro` | Purchase Order Navigator Pro | Browse purchase orders by date and vendor with Superbar Pro. | 20.0.24.12.04 |
| `app_sale_superbar` | App Sale Order Browse by Partner and Channel | Browse sale order by partner and sale channel with parent children tree navigator | 20.0.26.10.31 |
| `app_sale_superbar_pro` | Advance Sale Order Navigator by Partner and Channel | Advance browse sale orders by partner and channel with instant and lazy search mode | 20.0.24.12.04 |
| `app_stock_ztree` | Stock Location zTree Parent Children Tree | Stock location parent children tree selector in many2one field | 20.0.24.12.09 |
| `app_web_enterprise` | Enterprise UI Enhance Pack | Enterprise UI enhance with green theme, menu arrows, field underline and grid lines | 20.0.26.10.15 |
| `app_web_fullwidth` | Web Form Fullwidth & Chatter Position | Form responsive full screen with configurable chatter position | 20.0.25.04.05 |
| `app_website_product_superbar` | Website Product Browse by Category Superbar | Browse website products by category tree with parent children navigator | 20.0.24.11.12 |

### Base

| Technical Name | Module | Description | Version |
| --- | --- | --- | --- |
| `app_base_chinese` | odoo中国版中文本土化套件 | Chinese enhance with address format, timezone, currency, policy sensitivity. | 20.0.26.09.27 |
| `app_mixin_name_en` | Product english name with Mixin | Chinese enhance. Out of the box use in china. Set all chinese default value. Add quick set of english name. Default country, timezone, currency, partn… | 20.0.26.05.13 |
| `app_mrp_bom_product_multi_add` | MRP Bom Product Multi Batch Add | One click to batch add multiple products to MRP BOM with filter and group. | 20.0.25.09.16 |
| `app_mrp_production_zchart` | MRP Production zChart Hierarchy | Multi level MO hierarchy chart for MRP production order with N+1/N+2 subordinates. | 20.0.25.08.26 |
| `app_odoo_doc` | Odoo用户手册与开发手册 | 1-Click access to Odoo user & developer documentation of current topic, with local branding. | 20.0.26.10.25 |
| `app_saas` | odooapp.cn SaaS Client - Ai Passport | https://www.odooapp.cn/conditions | 20.0.26.10.27 |
| `app_sample` | Odoo Module Sample with Widget | Odoo module template with 170+ widget list and developer sample code | 20.0.24.12.26 |

## Installation

1. Add this directory to Odoo `addons_path` and restart the server.
2. Open Apps with developer mode and click "Update Apps List".
3. Search for the technical name and install. Dependencies are installed automatically.
4. Some modules require Odoo Enterprise or third-party modules; check the description and dependencies.

## License and Support

- Author: odooai.cn
- Website: <https://www.odooai.cn>
- Demo: <https://demo.odooapp.cn>
- Support: <odoo@china.com>
- License: see the `license` field in each `__manifest__.py` (LGPL-3 / OPL-1 and others).
