import { signal, toRaw, useEffect } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { localeCompare } from "@web/core/l10n/utils";
import { x2ManyCommands } from "@web/core/orm_plugin";
import { deepCopy } from "@web/core/utils/objects";
import { parseXML } from "@web/core/utils/xml";
import { patch } from "@web/core/utils/patch";
import { registry } from "@web/core/registry";
import { useSubEnv } from "@web/owl2/utils";
import { FormArchParser } from "@web/views/form/form_arch_parser";
// 原生模块未导出组件类：显式引入保证其先执行并完成注册，再从注册表取组件类
import "@web/webclient/res_user_group_ids_field/res_user_group_ids_field";

const { component: ResUserGroupIdsField } = registry
    .category("fields")
    .get("res_user_group_ids");

/**
 * Patch 原生 res_user_group_ids 字段小部件（web.ResUserGroupIdsField）：
 *  - res.groups.privilege 含多个 group_ids 时：沿用原生 selection 下拉样式，同 scope 内互斥；
 *  - res.groups.privilege 仅含一个 group_id 时：渲染为 boolean 复选框，各 scope 之间互不互斥；
 *  - 无 privilege_id 的组：保持原生行为（Extra Rights，仅开发者模式显示）。
 *
 * 原生 setup 中字段生成与取值逻辑为内联代码，故整体替换 setup 与 onRecordChanged；
 * 模板、注册表项及其余方法（getFieldName/getCategoryArch/getExtraGroupsArch 等）均复用原生实现。
 */
patch(ResUserGroupIdsField.prototype, {
    setup() {
        const { groups, privileges, categories } = toRaw(
            this.props.record.data.view_group_hierarchy
        );

        // Generate the "other" category (for privileges that do not belong to any category)
        const privilegesWithoutCategory = Object.values(privileges)
            .filter((privilege) => !privilege.category_id)
            .sort((privilege) => privilege.sequence);
        if (privilegesWithoutCategory.length) {
            categories.push({
                id: "other",
                name: _t("Other"),
                privilege_ids: privilegesWithoutCategory.map((privilege) => privilege.id),
            });
        }

        // Generate the extra rights category (for groups without privilege)
        this.extraCategory = {
            id: "extra",
            name: _t("Extra Rights"),
            privileges: Object.values(groups)
                .filter((group) => !group.privilege_id)
                .map((group) => {
                    const privilege = {
                        description: group.comment,
                        groupId: group.id,
                        id: "group_" + group.id,
                        name: group.name,
                    };
                    privilege.groupFieldName = this.getFieldName(privilege);
                    return privilege;
                })
                .sort((p1, p2) => localeCompare(p1.name, p2.name)),
        };

        // Generate selection (multi-group privileges) and boolean (single-group
        // privileges and extra right groups) fields
        this._fields = {};
        const booleanFieldToGroupId = {};
        for (const category of categories) {
            category.privileges = [];
            for (const privilegeId of category.privilege_ids) {
                const privilege = privileges[privilegeId];
                category.privileges.push(privilege);
                const helpLines = privilege.description ? [privilege.description] : [];
                const groupIds = privilege.group_ids;
                if (groupIds.length === 1) {
                    // 单组 scope：渲染为独立复选框（非互斥），字段名沿用 field_<pid>
                    const gid = groupIds[0];
                    if (groups[gid].comment) {
                        helpLines.push(`- ${groups[gid].name}: ${groups[gid].comment}`);
                    }
                    const fieldName = this.getFieldName(privilege);
                    this._fields[fieldName] = {
                        help: helpLines.join("\n"),
                        string: groups[gid].name || privilege.name,
                        type: "boolean",
                    };
                    booleanFieldToGroupId[fieldName] = gid;
                } else {
                    for (const gid of groupIds) {
                        if (groups[gid].comment) {
                            helpLines.push(`- ${groups[gid].name}: ${groups[gid].comment}`);
                        }
                    }
                    const selection = groupIds.map((gId) => [gId, groups[gId].name]);
                    selection.unshift([false, privilege.placeholder || ""]);
                    this._fields[this.getFieldName(privilege)] = {
                        help: helpLines.join("\n"),
                        selection,
                        string: privilege.name,
                        type: "selection",
                    };
                }
            }
        }
        for (const privilege of this.extraCategory.privileges) {
            this._fields[privilege.groupFieldName] = {
                help: privilege.description,
                string: privilege.name,
                type: "boolean",
            };
            booleanFieldToGroupId[privilege.groupFieldName] = privilege.groupId;
        }
        this.fields = deepCopy(this._fields); // dynamically modifed before each rendering w.r.t. to current groups
        this.booleanFieldToGroupId = booleanFieldToGroupId;

        // Generate archInfo to provide to the FormRenderer
        const models = { main: { fields: this._fields } };
        const arch = `
            <t>
                <group>
                    ${categories.map((category) => this.getCategoryArch(category)).join("")}
                </group>
                ${this.debugMode.isActive() ? this.getExtraGroupsArch() : ""}
            </t>`;
        this.archInfo = new FormArchParser().parse(parseXML(arch), models, "main");

        // Generate information to share through the env with "res_user_group_ids_privilege" widgets
        //  - `booleanFieldToGroupId` maps generated boolean field names to their group id
        //  - `privileges` is an object mapping all privilege ids to their description
        //  - `groups` is an object mapping all group ids to their description, which is based on
        //     the current selected groups
        this.info = {
            booleanFieldToGroupId,
            groups: {},
            privileges,
        };
        useSubEnv({
            resUserGroupsInfo: this.info,
        });
        this.values = signal({});
        this.shadowedGroupIds = [];
        useEffect(() => {
            // Generate groups information based on current ids, i.e.
            //  - `id`, `name`, `privilege_id`, `comment` are kept as in the static definition
            //  - `selected` is true iff the group is explicitely selected (!= implied)
            //  - `impliedByIds` only contain *selected* group ids that imply the given group
            //  - `disjointIds` is only set for *selected* or *implied* groups
            //  - `implyIds` doesn't contain itself, because it's useless and easier later
            const selectedIds = new Set(this.props.record.data[this.props.name].currentIds);
            for (const group of Object.values(groups)) {
                const selected = selectedIds.has(group.id);
                this.info.groups[group.id] = {
                    name: group.name,
                    id: group.id,
                    privilege_id: group.privilege_id,
                    comment: group.comment,
                    impliedByIds: group.all_implied_by_ids.filter(
                        (gid) => gid !== group.id && selectedIds.has(gid)
                    ),
                    implyIds: selected
                        ? group.all_implied_ids.filter((gid) => gid !== group.id)
                        : [],
                    selected,
                };
            }
            for (const group of Object.values(groups)) {
                let disjointIds = [];
                const { selected, impliedByIds } = this.info.groups[group.id];
                if (selected || impliedByIds.length) {
                    disjointIds = group.disjoint_ids.filter(
                        (gid) =>
                            this.info.groups[gid].selected ||
                            this.info.groups[gid].impliedByIds.length
                    );
                }
                this.info.groups[group.id].disjointIds = disjointIds;
            }

            // Remove lower level groups from selection fields where a higher level group is implied
            for (const fieldName in this.fields) {
                if (this.fields[fieldName].type === "selection") {
                    const options = this._fields[fieldName].selection;
                    this.fields[fieldName].selection = options;
                    for (let i = options.length - 1; i > 0; i--) {
                        // i > 0 to omit "false" option
                        const group = this.info.groups[options[i][0]];
                        const isImplied = group.impliedByIds.some(
                            (gid) => this.info.groups[gid].privilege_id !== group.privilege_id
                        );
                        if (isImplied) {
                            this.fields[fieldName].selection = options.slice(i);
                            break;
                        }
                    }
                }
            }

            // Generate values for the dynamically generated selection and boolean fields
            const values = {};
            const shadowedGroupIds = [];
            for (const category of categories) {
                for (const privilege of category.privileges) {
                    const fieldName = this.getFieldName(privilege);
                    if (this._fields[fieldName].type === "boolean") {
                        // 单组 scope：直接取该组是否被显式勾选
                        values[fieldName] = selectedIds.has(privilege.group_ids[0]);
                        continue;
                    }
                    let groupId =
                        privilege.group_ids.findLast((gId) => selectedIds.has(gId)) || false;
                    const options = this.fields[fieldName].selection;
                    if (groupId && !options.some((option) => option[0] === groupId)) {
                        // The option has been removed because a higher level group is implied
                        // => force the value to false to show the implied group instead
                        shadowedGroupIds.push(groupId);
                        groupId = false;
                    }
                    values[fieldName] = groupId;
                }
            }
            if (this.extraCategory) {
                for (const privilege of this.extraCategory.privileges) {
                    values[this.getFieldName(privilege)] = selectedIds.has(privilege.groupId);
                }
            }
            this.shadowedGroupIds = shadowedGroupIds;
            this.values.set(values);
        });

        this.hooks = {
            onRecordChanged: this.onRecordChanged.bind(this),
        };
    },

    onRecordChanged(_, values) {
        let selectedGroupIds = [];
        for (const [fieldName, val] of Object.entries(values)) {
            const field = this.fields[fieldName];
            if (!field) {
                continue;
            }
            if (field.type === "selection" && val) {
                selectedGroupIds.push(val);
            } else if (field.type === "boolean" && val) {
                // 单组 scope 复选框与 Extra Rights 复选框统一处理
                const gid = this.booleanFieldToGroupId[fieldName];
                if (gid) {
                    selectedGroupIds.push(gid);
                }
            }
        }
        // Keep shadowed groups, except if an higher level group has been set, in which case they
        // are not shadowed anymore
        const { groups, privileges } = this.info;
        const shadowedGroupIds = this.shadowedGroupIds.filter(
            (gid) => !values[this.getFieldName(privileges[groups[gid].privilege_id])]
        );
        selectedGroupIds = selectedGroupIds.concat(shadowedGroupIds);
        return this.props.record.update({
            [this.props.name]: [x2ManyCommands.set(selectedGroupIds)],
        });
    },
});
