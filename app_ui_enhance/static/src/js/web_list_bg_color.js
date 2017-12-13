odoo.define('app_ui_enhance.list_bg_color', function (require) {
"use strict";

var core = require('web.core');
var common = require('web.form_common');
var Model = require('web.Model');
var time = require('web.time');
var ListView = require('web.ListView');
var session = require('web.session');
var compatibility = require('web.compatibility');

    ListView.include({
        willStart: function() {
            if (this.fields_view.arch.attrs.bg_colors) {
                this.bg_colors = _(this.fields_view.arch.attrs.bg_colors.split(';')).chain()
                    .compact()
                    .map(function(color_pair) {
                        var pair = color_pair.split(':'),
                            color = pair[0],
                            expr = pair[1];
                        return [color, py.parse(py.tokenize(expr)), expr];
                    }).value();
                
                if (!this.colors) { this.colors = [] }
            }
            return this._super();
        },

        style_for: function (record) {
            var len, style= '';

            var context = _.extend({}, record.attributes, {
                uid: session.uid,
                current_date: moment().format('YYYY-MM-DD')
                // TODO: time, datetime, relativedelta
            });

            var i;
            var pair;
            var expression;
            style = this._super(record);
     
            if (!this.bg_colors) { return style; }
            for(i=0, len=this.bg_colors.length; i<len; ++i) {
                pair = this.bg_colors[i];
                var color = pair[0];
                expression = pair[1];
                if (py.PY_isTrue(py.evaluate(expression, context))) {
                    return style += 'background-color: ' + color + ';';
                }
            }
            return style;
        },

    });
    
});
