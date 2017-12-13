odoo.define('web.inputmask_widget', function (require) {
    "use strict";
    var core = require('web.core');
    var formats = require('web.formats');
    var form_widgets = require('web.form_widgets');
    var kanban_widgets = require('web_kanban.widgets');
    var utils = require('web.utils');
    var list_widget_registry = core.list_widget_registry;
    var QWeb = core.qweb;

    function mask_attrs(attrs) {
        var keyMask = 'data-inputmask';
        var attributes = {};
        if (keyMask in attrs)
            attributes[keyMask] = attrs[keyMask];
        else
            attributes = Object.keys(attrs).reduce(function (filtered, key) {
                if (key.indexOf(keyMask) !== -1)
                    filtered[key] = attrs[key];
                return filtered;
            }, {});
        if (!attributes)
            console.warn("The widget Mask expects the 'data-inputmask[-attribute]' attributes!")
        return attributes;
    }

    var FieldMask = form_widgets.FieldChar.extend({
        template: "FieldMask",
        attributes: {},
        init: function (field_manager, node) {
            this._super(field_manager, node)
            this.attributes = mask_attrs(node.attrs);
        },
        render_value: function (mask) {
            this._super();
            if (this.attributes) {
                if (this.$input !== undefined)
                    this.$input.inputmask(mask);
                else if ('contenteditable' in this.node.attrs)
                    this.$el.inputmask(mask);
            }
        },
        //在前端验证输入值是否符合inputmask
        is_valid: function () {
            var musk = this.attributes['data-inputmask-regex'] ? this.attributes['data-inputmask-regex'] : this.attributes['data-inputmask'] ;
            var reg = new RegExp (musk,"g");
            var value = this.$input.val();
            if (!this.get('required') && this.is_false())   {
                return true;
            }   else if (reg.test(value)) {
                return true;
            } else {
                return false;
            }
        },
    });

    var FieldMaskRegex = FieldMask.extend({
        render_value: function () {
            this._super("Regex");
        }
    });

    var ColumnMask = list_widget_registry.get('field.char').extend({
        attributes: {},
        $mask: undefined,
        init: function (id, tag, attrs) {
            this._super(id, tag, attrs);
            this.attributes = mask_attrs(attrs);
            if (this.attributes)
                this.$mask = $(jQuery.parseHTML(QWeb.render('Widget.mask', {widget: this}))).inputmask(undefined, {
                    placeholder: '',
                    greedy: false
                });
        },
        format: function (row_data, options) {
            var value = this._super(row_data, options);
            if (this.$mask) {
                this.$mask.val(value);
                value = this.$mask.val();
            }
            return value;
        }
    });

    var MaskWidget = kanban_widgets.AbstractField.extend({
        tagName: 'span',
        attributes: {},
        init: function (parent, field, $node) {
            this._super(parent, field, $node);
            this.attributes = mask_attrs(field.__attrs);
            if (this.attributes)
                this.$mask = $(jQuery.parseHTML(QWeb.render('Widget.mask', {widget: this}))).inputmask(undefined, {
                    placeholder: '',
                    greedy: false
                });
        },
        renderElement: function () {
            var value = this.field.raw_value;
            if (this.$mask)
                this.$mask.val(value);
            value = this.$mask.val();
            this.$el.text(value);
        }
    });

    core.form_widget_registry.add('mask', FieldMask);
    core.form_widget_registry.add('mask_regex', FieldMaskRegex);
    list_widget_registry.add('field.mask', ColumnMask);
    kanban_widgets.registry.add("mask", MaskWidget);

    return {FieldMask: FieldMask, FieldMaskRegex: FieldMaskRegex, MaskWidget: MaskWidget};
});
