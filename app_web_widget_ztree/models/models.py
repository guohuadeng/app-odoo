# -*- coding: utf-8 -*-
from odoo import models, api


class BaseModelExtend(models.AbstractModel):
    _name = 'basemodel.extend'
    _description = 'Base Extend for Ztree'


    def _register_hook(self):
        """
        Register method in BaseModel
        type: bar是在superbar中，field是在form中
        """
        # name_field 显示的字段
        # type = chart 时，只取自己这棵树，使用 parent_path 处理
        @api.model
        def search_ztree(self, domain=None, context=None, parent_key=None, root_id=None, expend_level=None, name_field=None, limit=None, order=None, type=None,
                         selected_id=None):
            if context:
                self = self.with_context
            try:
                limit = int(limit)
            except Exception:
                limit = 1000
            if not limit:
                limit = 1000
            if not order:
                order = self._order
            try:
                expend_level = int(expend_level)
                if expend_level == 0:
                    expend_level = 3
            except Exception:
                expend_level = 3
            
            if name_field:
                pass
            elif self._fields.get("name"):
                name_field = 'name'
            elif self._fields.get("display_name"):
                name_field = 'display_name'
            else:
                name_field = self._rec_name

            if name_field == 'display_name':
                fields = ['id', 'display_name']
            else:
                fields = ['id', name_field, 'display_name']

            # 返回 id, name, value, pId, title, value
            def ztree(x):
                y = {}
                p = parent_key
                pid = False
                if p and x.get(p):
                    pid = x[p]
                    if pid:
                        pid = pid[0]
                y['id'] = x['id']
                if x.get(name_field):
                    y['name'] = x[name_field]
                else:
                    y['name'] = x['display_name']

                y['value'] = x[name_field]
                y['title'] = x['display_name']
                y['pId'] = pid
                return y

            # 递归展开指定级别，即设定open
            def getLevel(node, nodes, level=1):
                if not node.get("pId"):
                    level = 1
                else:
                    try:
                        level = level + getLevel(nodes[node.get("pId")], nodes)
                    except Exception:
                        level = 1
                return level

            # todo: 检查 root_id 的处理
            if not parent_key:
                parent_key = self._parent_name or False
            if parent_key:
                fields.append(parent_key)
                if root_id:
                    r = self.search_read([('id', '=', root_id)], ['parent_path'], limit=1)
                    path = r[0]['parent_path']
                    domain += [('parent_path', '=like', path + '%')]
                #     type=chart时 遍历只取本棵树
                elif type == 'chart' and not selected_id:
                    # 没有当前值，比如创建时，显示空
                    domain += [('id', '=', False)]
                elif type == 'chart' and not self._fields.get("parent_path"):
                    # 没有parent_path，只显示当前
                    domain += [('id', '=', selected_id)]
                elif type == 'chart' and selected_id:
                    r = self.search_read([('id', '=', selected_id)], ['parent_path'], limit=1)
                    if r:
                        path = r[0]['parent_path']
                        pos = path.find('/')
                        if pos > 0:
                            path = path[0:pos + 1]
                            domain += [('parent_path', '=like', path + '%')]
                    else:
                        domain += [('id', '=', selected_id)]
            records = self.search_read(domain or [], fields, 0, limit=limit, order=order)

            if not records:
                return []

            result = records
            res = map(ztree, result)

            if len(result) < 1:
                return result

            # reorder read, index: dict,  res: list
            index = {vals['id']: vals for vals in res}
            for key in index:
                index[key]["ztree_link"] = '/mail/view?model=%s&res_id=%s' % (self._name, index[key]["id"]),
                index[key]["level"] = getLevel(index[key], index, 1)
                if index[key]["level"] < expend_level:
                    index[key]["open"] = True
                else:
                    index[key]["open"] = False

            res = [index[record["id"]] for record in records if record["id"] in index]
            return res

        models.BaseModel.search_ztree = search_ztree
        return super(BaseModelExtend, self)._register_hook()
