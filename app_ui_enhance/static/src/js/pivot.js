odoo.define('app_ui_enhance.pivot', function (require) {
"use strict";

var time        = require('web.time');
var core        = require('web.core');
var data        = require('web.data');
var session     = require('web.session');
var utils       = require('web.utils');
var Model       = require('web.Model');
var PivotView   = require('web.PivotView');
var datepicker  = require('web.datepicker');

var _t = core._t;
var _lt = core._lt;
var QWeb = core.qweb;

PivotView.include({

    init: function() {
        this._super.apply(this, arguments);        
        this.ts_fields = [];
    },

    tgl_on_button_click: function (event) {
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
        var ts_context = this.context.tree_search;

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

        $(QWeb.render("odooApp.TreeSearch.Placeholder", {})).appendTo($node);

        var date_fields = [];
        var canShow = 1;
        // 增加参数控制app_ui_show_search_date,特殊处理
        new Model('ir.config_parameter').call('search_read', [[['key', '=', 'app_ui_show_search_date']], ['value']]).then(function (show) {
            if (show.length >= 1 && (show[0]['value'] == "False")) {
                canShow = 0;
            }
            if (canShow) {
                _.each(self.fields, function (value, key, list) {
                    if (value.store && value.type === "datetime" || value.type === "date") {
                        date_fields.push([key, value.string]);
                    }
                });
                if (date_fields.length > 0) {
                    self.$search_date = $(QWeb.render('odooApp.SearchDate', {'date_fields': date_fields}))
                    self.$search_date.find('.app_start_date').datetimepicker(datepickers_options);
                    self.$search_date.find('.app_end_date').datetimepicker(datepickers_options);

                    self.$search_date.find('.app_start_date').on('keypress', function (e) {
                        self.do_keypress(e);
                    });
                    self.$search_date.find('.app_end_date').on('keypress', function (e) {
                        self.do_keypress(e);
                    });
                    setTimeout(function(){
                        self.$search_date.appendTo($('.o_cp_buttons'));
                        self.set_search_btn(1);
                    }, 1000);
                }
            }
        });

        var number_fields = [];

        // 增加参数控制app_ui_show_search_number
        new Model('ir.config_parameter').call('search_read', [[['key', '=', 'app_ui_show_search_number']], ['value']]).then(function (show) {
            if (show.length >= 1 && (show[0]['value'] == "True")) {
                number_fields = [];
                _.each(self.fields, function (value, key, list) {
                    if (value.string && value.string.length > 1 && value.store && (value.type === "integer" || value.type === "float" || value.type === "monetary")) {
                        number_fields.push([key, value.string]);
                    }
                });

                if (number_fields.length > 0) {
                    self.$search_number = $(QWeb.render('odooApp.SearchNumber', {'number_fields': number_fields}))

                    self.$search_number.find('.app_start_number').on('keypress', function (e) {
                        self.do_keypress(e);
                    });
                    self.$search_number.find('.app_end_number').on('keypress', function (e) {
                        self.do_keypress(e);
                    });
                    setTimeout(function(){
                        self.$search_number.appendTo($('.o_cp_buttons'));
                        self.set_search_btn(1);
                    }, 1000);
                }
            }
        });
        //显示搜索键，因为pivot特殊，故要单独处理
    },

    set_search_btn: function (show) {
        var self = this;
        if (self.$search_btn) {
            self.$search_btn.remove();
        }
        if (show) {
            self.$search_btn = $(QWeb.render("odooApp.odooapp-btn", {})).appendTo($('.o_cp_buttons'));
            self.$search_btn.children('.odooapp-search-btn').on('click', function () {
                self.tgl_search();
            });
            self.$search_btn.children('.odooapp-clear-btn').on('click', function () {
                self.do_clear();
            });
        }
    },

    do_search: function(domain, context, group_by) {        
        var self = this;
        this.last_domain = domain;
        this.last_context = context;
        this.last_group_by = group_by;
        this.old_search = _.bind(this._super, this);
        return self.tgl_search();
    },

    do_keypress: function(e) {
        var self = this;
        var keynum = window.event ? e.keyCode : e.which;
        if (keynum==13)
            return self.tgl_search();
    },

    do_clear: function() {
        var self = this;
        if (self.$search_date) {
            self.$search_date.find('.app_start_date').val('');
            self.$search_date.find('.app_end_date').val('');
        }
        if (self.$search_number) {
            self.$search_number.find('.app_start_number').val('');
            self.$search_number.find('.app_end_number').val('');
        }
        return self.tgl_search();
    },

    tgl_search: function() {
        var self = this;
        var domain = [], value, value_tmp;

        _.each(self.ts_fields, function(field){
            value = $('.app_item_' + field).val();

            var select_fields = $('.app_multi_item_' + field).children('.selected'),
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
        });

// 注意，date和datetime型的处理是不同的，已处理完
        if (self.$search_date) {
            var start_date  = self.$search_date.find('.app_start_date').val(),
                end_date    = self.$search_date.find('.app_end_date').val(),
                field       = self.$search_date.find('.app_select_field').val(),
                field_type  = 'datetime';
            var tz = session.user_context.tz,
                start_utc,
                end_utc;

            _.each(self.columns, function (value, key, list) {
                if (value.name == field) {
                    field_type = value.type;
                    return false;
                }
            });

            moment.locale(tz);
            var l10n = _t.database.parameters;
            if (start_date) {
                if (field_type  == 'date')   {
                    //日期类型，无须utc处理
                    start_date = moment(moment(start_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD');
                    domain.push([field, '>=', start_date]);
                }   else {
                    //日期时间，处理utc
                    start_date = moment(moment(start_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD 00:00:00');
                    start_utc = moment(start_date)
                    domain.push([field, '>=', start_utc]);
                }
            }
            if (end_date) {
                if (field_type  == 'date')   {
                    end_date = moment(moment(end_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD');
                    domain.push([field, '<=', end_date]);
                }   else {
                    end_date = moment(moment(end_date, time.strftime_to_moment_format(l10n.date_format))).format('YYYY-MM-DD 00:00:00');
                    end_utc = moment(end_date)
                    domain.push([field, '<=', end_utc]);
                }
            }
        }

        if (self.$search_number) {
            var start_range  = self.$search_number.find('.app_start_number').val(),
                end_range    = self.$search_number.find('.app_end_number').val(),
                range_field  = self.$search_number.find('.app_select_range_field').val();

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