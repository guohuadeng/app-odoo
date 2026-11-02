# app-odoo 模块集（Odoo 20）

> odooai.cn 的 Odoo 20 模块集合，共 **55** 个模块。
> 每个模块目录包含 `__manifest__.py` 与 `static/description/`（index.html、index_cn.html、banner.png、banner_cn.png 等描述资源）。

## 目录结构

```
app-odoo/
  app_xxx/
    __manifest__.py
    models/ views/ data/ security/
    static/description/   # 应用商店描述页、Banner、截图
```

## 模块清单

模块按 Odoo 分类分组，说明取自各模块 `__manifest__.py` 的 `summary`。

### 销售（Sales）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_sale_product_multi_add` | 销售订单批量添加产品 | 一键批量将多个产品添加到销售订单，支持过滤、分组和明细录入。 | 20.0.24.12.03 |

### 库存（Inventory）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_purchase_product_multi_add` | 采购订单批量添加产品 | 一键批量将多个产品添加到采购订单，支持过滤、分组和明细录入。 | 20.0.24.12.03 |
| `app_stock_picking_product_multi_add` | 库存调拨单批量添加产品 | 一键批量将多个产品添加到库存调拨单 | 20.0.24.12.03 |
| `app_stock_superbar` | 库存超级搜索栏 | 按库存位置和类型树状导航，支持调拨单、批次、移动线 | 20.0.25.09.08 |
| `app_stock_superbar_pro` | 库存高级超级搜索栏 | 库存高级搜索，支持日期搜索和父子树导航 | 20.0.25.09.08 |

### 会计（Accounting）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_account_invoice_product_multi_add` | 客户发票与供应商账单批量添加产品,Account Invoice Product Multi Add | 一键批量将多个产品添加到客户发票与供应商账单中，支持过滤与分组。 | 20.0.24.12.03 |
| `app_account_superbar` | 会计科目树状导航,Account Superbar Navigator | 会计科目树状导航，按科目表结构浏览日记账、凭证行、辅助核算。 | 20.0.26.08.21 |
| `app_account_ztree` | 多层级会计科目树,Account Multi Level Chart Tree | 会计科目多层级父子树状选择器，zTree widget。 | 20.0.26.10.08 |
| `l10n_cn_standard_latest` | 2027最新中国会计科目表 | 2027最新中国会计科目表（含小规模纳税人），营改增后会计科目调整，多级科目支持 | 20.0.26.10.28 |

### 人力资源（Human Resources）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_hr_expense_superbar` | Hr Expense Superbar | Browse hr expense by departments or Analytic Account. Easy to navigator and browse any data. Support list, kanban, pivot, graph view. ztree widget. hr… | 20.0.26.05.20 |
| `app_hr_expense_superbar_pro` | Hr Expense Superbar Pro | Browse hr expense by departments or Analytic Account. Easy to navigator and browse any data. Support list, kanban, pivot, graph view. ztree widget. hr… | 20.0.26.10.23 |
| `app_hr_superbar` | HR员工部门导航 | 按部门树形浏览员工，Superbar高级搜索，组织架构图。 | 20.0.24.11.12 |

### 网站（Website）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_ai_bard` | 谷歌Gemini AI支持,Google Gemini (Bard) AI for Odoo | Odoo AI中心集成Google Gemini(Bard)AI，支持多AI机器人对话与训练。 | 20.0.26.10.21 |
| `app_chatgpt` | AI服务中心聚合全网AI,ChatGPT DeepSeek Ali Qwen AiGC Center | Odoo AI中心，集成ChatGPT4、DeepSeek、阿里通义千问、百度文心等多种AI。 | 20.0.26.10.12 |
| `app_claude` | Claude AI集成 | Ai服务中心的Claude支持，包括Claude Opus 4.1、Claude Sonnet 4.5、Claude Haiku等模型，本版本支持对话模型。 | 20.0.26.10.12 |
| `app_deepseek` | 深度求索AI集成 | Ai服务中心的DeepSeek支持，包括V3和R1等，本版本只支持开放对话模型。 | 20.0.26.10.12 |
| `app_website_blog_editor` | 网站博文源码编辑器 | 源码方式编辑网站页面和博客，批量编辑和SEO优化 | 20.0.26.10.21 |
| `app_website_blog_superbar` | 网站博文超级搜索栏 | 网站博文增强搜索，树状导航浏览博客文章 | 20.0.24.11.12 |
| `app_website_sale_editor` | 电商产品源码编辑器 | 源码方式编辑电商产品页面，批量SEO优化 | 20.0.26.10.14 |

### 零售 POS（Point of Sale）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_pos_superbar` | POS销售单导航 | 按门店、销售员和状态浏览POS订单，Superbar高级搜索。 | 20.0.25.06.10 |

### 技术（Technical）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_odoo_sync` | 实例数据同步（Odoo 18 → 20）,Odoo Instance Data Sync | 从 Odoo 18 线上实例只读拉取用户与往来数据，保 id/保 xml_id/可增量/可重复执行。 | 20.0.26.10.31 |

### 扩展工具（Extra Tools）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_odoo_customize` | Odoo20 Tweak OEM Development Enhance.Boost,Customize,Ai Employee,UI,Security,Remove Data All in One-优化提速65+项大全 | 60+ Odoo Enhance in 1 click Tweak odoo. Change Odoo to your OEM brand.all in one odoo enhancement. for Customize,UI,Boost Security,Development. ChatWi… | 20.0.26.10.29 |

### 扩展工具（Extra tools）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_auto_backup` | 数据库自动备份,Database Auto Backup and Download | Odoo数据库自动备份、远程SFTP备份、一键手动备份、备份文件下载管理。 | 20.0.26.09.20 |
| `app_base_company_zchart` | 集团公司多层级结构图,Group Company Multi Level Chart Hierarchy | 集团公司多层级树状结构图，zChart widget。 | 20.0.25.06.10 |
| `app_base_superbar` | 基础管理快速导航,Easy Admin Navigator with Superbar | 菜单/视图/字段/动作/用户等管理项快速树状导航。 | 20.0.26.09.15 |
| `app_common` | 欧度智能基础功能及面板,odooAi Common Util and Tools | odooai.cn应用核心基础模块，提供通用工具函数和面板。 | 20.0.26.10.13 |
| `app_contacts_superbar` | 通讯录联系人超级导航 | 按公司、类别、行业树状浏览联系人 | 20.0.26.10.15 |
| `app_contacts_superbar_pro` | 通讯录联系人超级导航专业版 | 增强版联系人导航，新增公司类型和日期范围搜索 | 20.0.24.12.04 |
| `app_crm_superbar` | CRM商机线索超级导航 | 按阶段、团队、营销活动树状浏览商机与线索 | 20.0.24.11.12 |
| `app_event_superbar` | 活动高级搜索导航,Event Advance Search Superbar | 按活动阶段和标签分类树状导航浏览活动。 | 20.0.25.06.10 |
| `app_event_superbar_pro` | 活动高级搜索 | 按阶段和日期浏览活动，Superbar高级搜索侧栏。 | 20.0.26.10.25 |
| `app_hr_ztree` | HR部门树形组件 | HR部门员工父子树形选择器，zTree组件。 | 20.0.24.12.09 |
| `app_mail_superbar` | 邮件高级搜索 | 按多种分类浏览邮件，Superbar高级搜索。 | 20.0.24.11.12 |
| `app_module_superbar` | 应用模块导航 | 按分类树形浏览应用和模块。 | 20.0.24.11.12 |
| `app_mrp_superbar` | MRP制造单导航 | 按物料可用性和工作中心浏览制造单，Superbar高级搜索。 | 20.0.25.06.10 |
| `app_product_category_zchart` | 产品目录层级图 | 产品目录多层级结构图组件，支持N+1/N+2级展示。 | 20.0.25.02.27 |
| `app_product_superbar` | 产品分类导航 | 按分类树形浏览产品，Superbar高级搜索。 | 20.0.26.09.09 |
| `app_product_superbar_pro` | 产品分类导航Pro版 | 产品分类高级搜索Pro增强版，更多功能特性。 | 20.0.25.04.19 |
| `app_product_ztree` | 产品分类树形组件 | 产品分类父子树形选择器，zTree组件。 | 20.0.24.12.09 |
| `app_project_superbar` | 项目任务导航 | 按公司、客户、用户和阶段浏览项目和任务。 | 20.0.26.08.18 |
| `app_purchase_superbar` | 采购超级搜索导航 | 采购订单按供应商树状导航，支持列表、看板、透视表、图表视图 | 20.0.26.08.19 |
| `app_purchase_superbar_pro` | 采购订单高级搜索Pro | 按日期和供应商浏览采购订单，Superbar Pro高级搜索。 | 20.0.24.12.04 |
| `app_sale_superbar` | 销售订单超级搜索栏 | 按客户和销售渠道浏览销售订单，树状层级导航 | 20.0.26.10.31 |
| `app_sale_superbar_pro` | 销售订单高级超级搜索栏 | 按客户和销售渠道高级浏览销售订单，即时和延迟搜索模式 | 20.0.24.12.04 |
| `app_stock_ztree` | 库存位置树控件 | 库存位置父子树选择器，在many2one字段中显示树状层级 | 20.0.24.12.09 |
| `app_web_enterprise` | Odoo 企业版界面增强 | 企业版界面增强套件，护眼绿色主色、菜单箭头、字段下划线、表格分隔线 | 20.0.26.10.15 |
| `app_web_fullwidth` | 表单全宽度满屏 | 表单全屏全宽显示，自定义备注消息位置 | 20.0.25.04.05 |
| `app_website_product_superbar` | 网站产品按分类超级搜索栏 | 按网站产品分类树状导航浏览产品 | 20.0.24.11.12 |

### 基础（Base）

| 模块技术名 | 模块名称 | 说明 | 版本 |
| --- | --- | --- | --- |
| `app_base_chinese` | odoo中国版中文本土化套件,Odoo Chinese Localization Enhance All in One | Odoo简体中文版全面增强，开箱即用的中国本土化。 | 20.0.26.09.27 |
| `app_mixin_name_en` | Product english name with Mixin，产品增加英文名字段-以Mixin方式的统一处理 | Chinese enhance. Out of the box use in china. Set all chinese default value. Add quick set of english name. Default country, timezone, currency, partn… | 20.0.26.05.13 |
| `app_mrp_bom_product_multi_add` | MRP Bom批量添加产品 | 一键批量将多个产品添加到制造BOM中，支持过滤和分组。 | 20.0.25.09.16 |
| `app_mrp_production_zchart` | MRP生产单层级图 | MRP制造单多层级结构图，支持N+1、N+2级直接下属展示。 | 20.0.25.08.26 |
| `app_odoo_doc` | Odoo用户手册与开发手册,从入门到精通,odoo User Doc & Developer Doc Anywhere | Odoo用户手册与开发手册一键访问。 | 20.0.26.10.25 |
| `app_saas` | SaaS云服务客户端 | AiSaas云服务，使用Ai通行证，一键实现全社交媒体统一登录SSO。 支持微信、抖音、QQ、淘宝、钉钉、支付宝、企业微信、Facebook、Google、微软Azure等整合登录。 在Odoo中获取最新的中文翻译（会员专属），获取当前Odoo模块最新版本更新等。 支持Odoo中文版在线更新及 ww… | 20.0.26.10.27 |
| `app_sample` | Odoo 模块开发模板 | Odoo模块开发模板，含170+Widget清单与使用样例 | 20.0.24.12.26 |

## 安装

1. 将本目录加入 Odoo 的 `addons_path`，重启 Odoo 服务。
2. 进入「应用」并开启开发者模式，点击「更新应用列表」。
3. 搜索模块技术名并安装；有依赖的模块会一并安装。
4. 部分模块需要 Odoo 企业版或第三方模块，请以模块说明与依赖为准。

## 许可与支持

- 作者：odooai.cn
- 官网：<https://www.odooai.cn>
- 演示：<https://demo.odooapp.cn>
- 支持：<odoo@china.com>
- 许可：各模块 `__manifest__.py` 的 `license` 字段为准（LGPL-3 / OPL-1 等）。
