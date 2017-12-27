odoo.define('search_by_date_range.tree', function (require) {
"use strict";

var time        = require('web.time');
var core        = require('web.core');
var data        = require('web.data');
var session     = require('web.session');
var utils       = require('web.utils');
var Model       = require('web.Model');
var ListView   = require('web.ListView');
var datepicker  = require('web.datepicker');
var ViewManager = require('web.ViewManager')
var _t = core._t;
var _lt = core._lt;
var QWeb = core.qweb;

ListView.include({

    init: function(parent, dataset, view_id, options) {
        this._super.apply(this, arguments);
        this.ts_context = dataset.context.tree_search;
        this.fields_range = dataset.context.fields_range;
        this.ts_fields = [];
    },

    on_button_click: function (event) {
        var self = this;
        var $target = $(event.target), 
            field, key, first_item;

        field   = $target.parent().data('field');
        key     = $target.parent().data('key');

        if (field == -1) {
            first_item = $target.parent().parent().children('.tgl_first_item.selected');   
            if (!first_item.length) {
                $target.parent().parent().children('li').removeClass('selected')
            }
        } else {
            first_item = $target.parent().parent().children('.tgl_first_item').removeClass('selected');
        }

        $target.parent().toggleClass('selected');
        this.tgl_search()
        event.stopPropagation();

    },

    render_buttons: function($node) {
        var self = this;
        this._super.apply(this, arguments);

        var l10n = _t.database.parameters;
        var datepickers_options = {
            pickTime: false,
            startDate: moment({ y: 1900 }),
            endDate: moment().add(200, "y"),
            calendarWeeks: true,
            icons : {
                time: 'fa fa-clock-o',
                date: 'fa fa-calendar',
                up: 'fa fa-chevron-up',
                down: 'fa fa-chevron-down'
               },
            language : moment.locale(),
            format : time.strftime_to_moment_format(l10n.date_format),
        }

        self.$buttons.find('.sky-search').remove();

        // Tim kiem theo khoang thoi gian

        var sky_fields = [];
        _.each(self.columns, function(value, key, list){
            if (value.store && value.type === "datetime" || value.type === "date") {
                sky_fields.push([value.name, value.string]);
            }
        });
        if (sky_fields.length > 0) {
            self.$search_button = $(QWeb.render('SkyERP.buttons', {'sky_fields': sky_fields}))
            self.$search_button.find('.sky_start_date').datetimepicker(datepickers_options);
            self.$search_button.find('.sky_end_date').datetimepicker(datepickers_options);
            // self.$search_button.find('.sky_search_date_rate').click(function() {
            //     self.tgl_search();
            // });
            self.$search_button.find('.sky_start_date').on('change', function() {
                self.tgl_search();
            });
            self.$search_button.find('.sky_end_date').on('change', function() {
                self.tgl_search();
            });
            self.$search_button.find('.sky_select_field').on('change', function() {
                self.tgl_search();
            });
            self.$search_button.appendTo(self.$buttons);
        }        


        sky_fields = [];
        _.each(self.columns, function(value, key, list){
            if (value.string && value.string.length > 1 && value.store && (value.type === "integer" || value.type === "float" || value.type === "monetary")) {
                sky_fields.push([value.name, value.string]);
            }
        });

        if (sky_fields.length == 0) {
            if (self.fields_range) {
                sky_fields = self.fields_range;
            }
        }

        if (sky_fields.length > 0) {
            self.$search_range = $(QWeb.render('SkyERP.SearchRange', {'sky_fields': sky_fields}))
            // self.$search_range.find('.sky_search_date_range').click(function() {
            //     self.tgl_search();
            // });
            self.$search_range.find('.sky_select_range_field').on('change', function() {
                self.tgl_search();
            });
            self.$search_range.find('.sky_start_range').on('change', function() {
                self.tgl_search();
            });
            self.$search_range.find('.sky_end_range').on('change', function() {
                self.tgl_search();
            });
            self.$search_range.appendTo(self.$buttons);
        }    

        // Dropdown list cho phep chon nhieu
        _.each(this.ts_context, function(item){
            var field = _.find(self.columns, function(column){
                return column.type == 'many2one' && column.relation && column.name === item.name;
            });
            if (field) {
                self.ts_fields.push(item.name);
                new Model(field.relation).query(['id', 'display_name']).filter(new data.CompoundDomain(item.domain, field.domain)).context(new data.CompoundContext()).all().then(function (result) {
                    // var single_search = $(QWeb.render('SkyERP.selection', {
                    //     'string': item.string,
                    //     'class_name': 'sky_item_' + item.name,
                    //     'fields': result,
                    // }));
                    if (!$('.after_control_panel').length) {
                        // $(QWeb.render('SkyERP.after_control_panel', {})).appendTo($('.o_control_panel'));
                        // $(QWeb.render('SkyERP.after_control_panel', {})).appendTo($('.o_cp_left'));
                        
                        // $(QWeb.render('SkyERP.after_control_panel', {})).appendTo(self.$buttons);

                        var multi_search = $(QWeb.render("TGL.TreeSearch.Item", {'widget': {
                            'string': item.string,
                            'key': item.name,
                            'class_name': 'sky_multi_item_' + item.name,
                            'fields': result,
                        }}))

                        multi_search.find('li').click(self.on_button_click.bind(self));
                        multi_search.appendTo(self.$buttons);
                    }
                    // single_search.appendTo($('.after_control_panel'));
                    // $('.sky_item_' + item.name).on('change', function() {
                    //     self.tgl_search();
                    // })
                });
            }
        });
// {'tree_search': [{'string': 'Địa điểm', 'name': 'location_id', 'domain': [('usage', '=', 'internal')]}, {'string': 'Nhóm sản phẩm', 'name': 'categ_id', 'domain': []}]}        
// {'search_default_sales': 1, 'tree_search': [{'string': 'Địa điểm', 'name': 'location_id', 'domain': [('usage', '=', 'internal')]}, {'string': 'NV bán hàng', 'name': 'user_id', 'domain': []}]}        
// {'tree_search': [{'string': 'Địa điểm', 'name': 'location_id', 'domain': [('usage', '=', 'internal')]}]}
        // var a = $(QWeb.render('SkyERP.selection', {'class_name': 'abc','fields': [['1', '1'], ['2', '2']]}));
        // a.appendTo(self.$buttons);

    },  

    do_search: function(domain, context, group_by) {
        var self = this;
        this.last_domain = domain;
        this.last_context = context;
        this.last_group_by = group_by;
        this.old_search = _.bind(this._super, this);
        return self.tgl_search();
    },

    tgl_search: function() {
        var self = this;
        var domain = [], value, value_tmp;

        _.each(self.ts_fields, function(field){
            value = $('.sky_item_' + field).val();

            var select_fields = $('.sky_multi_item_' + field).children('.selected'),
                select_value = [];
            if (select_fields.length > 0) {
                _.each(select_fields, function(item){
                    value_tmp = $(item).data('field');
                    if (value_tmp > 0) {
                        select_value.push($(item).data('field'));
                    }
                });
                if (select_value.length) {
                    domain.push([field, 'in', select_value]);
                }

            }
            // if (value) {
            //     value_tmp = parseInt(value);
            //     if (value_tmp != 0) {
            //         domain.push([field,'=',value_tmp]);
            //     } else {
            //         domain.push([field,'!=', false]);
            //     }
            // }
        });

        if (self.$search_button) {
            var start_date  = self.$search_button.find('.sky_start_date').val(),
                end_date    = self.$search_button.find('.sky_end_date').val(),
                field       = self.$search_button.find('.sky_select_field').val();
            
            var l10n = _t.database.parameters;
            if (start_date) {
                start_date = moment(moment(start_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD');
                domain.push([field, '>=', start_date]);
            }
            if (end_date) {
                end_date = moment(moment(end_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD');
                domain.push([field, '<=', end_date]);
            }

        }

        if (self.$search_range) {
            var start_range  = self.$search_range.find('.sky_start_range').val(),
                end_range    = self.$search_range.find('.sky_end_range').val(),
                range_field  = self.$search_range.find('.sky_select_range_field').val();

            if (start_range) {
                domain.push([range_field, '>=', parseInt(start_range)]);
            }
            if (end_range) {
                domain.push([range_field, '<=', parseInt(end_range)]);
            }
        }
        // console.log(domain);
        var compound_domain = new data.CompoundDomain(self.last_domain, domain);
        self.dataset.domain = compound_domain.eval();
        return self.old_search(compound_domain, self.last_context, self.last_group_by);
    },

});

});