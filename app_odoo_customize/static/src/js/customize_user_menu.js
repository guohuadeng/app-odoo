odoo.define('app_odoo_customize.UserMenu', function (require) {
    "use strict";

    /**
     * This widget is appended by the webclient to the right of the navbar.
     * It displays the avatar and the name of the logged user (and optionally the
     * db name, in debug mode).
     * If clicked, it opens a dropdown allowing the user to perform actions like
     * editing its preferences, accessing the documentation, logging out...
     */

    const session = require('web.session');
    var UserMenu = require('web.UserMenu');
    //避免错误，要再定义
    var documentation_url = 'https://www.sunpop.cn';
    var documentation_dev_url = 'https://www.sunpop.cn';
    var support_url = 'https://www.sunpop.cn';
    var account_title = 'My Account';
    var account_url = 'https://www.sunpop.cn';

    UserMenu.include({
        init: function () {
            this._super.apply(this, arguments);
            var self = this;
            var session = this.getSession();
            var lang_list = '';
            self.is_manager = false;
            self.show_debug = false;

            self._rpc({
                model: 'res.lang',
                method: 'search_read',
                domain: [],
                fields: ['name', 'code'],
                lazy: false,
            }).then(function (res) {
                _.each(res, function (lang) {
                    var a = '';
                    if (lang['code'] === session.user_context.lang) {
                        a = '<i class="fa fa-check"></i>';
                    } else {
                        a = '';
                    }
                    lang_list += '<a role="menuitem" href="#" class="dropdown-item" data-lang-menu="lang" data-lang-id="' + lang['code']
                        + '"><img class="flag" src="app_odoo_customize/static/src/img/flags/' + lang['code'] + '.png"/>' + lang['name'] + a + '</a>';
                });
                lang_list += '<div role="separator" class="dropdown-divider"/>';
                setTimeout( function() {
                    $('switch-lang').replaceWith(lang_list);
                }, 1000);
            })

            //取参数
            self._rpc({
                model: 'ir.config_parameter',
                method: 'search_read',
                domain: [['key', '=like', 'app_%']],
                fields: ['key', 'value'],
                lazy: false,
            }).then(function (res) {
                $.each(res, function (key, val) {
                    if (val.key == 'app_documentation_url')
                        documentation_url = val.value;
                    if (val.key == 'app_documentation_dev_url')
                        documentation_dev_url = val.value;
                    if (val.key == 'app_support_url')
                        support_url = val.value;
                    if (val.key == 'app_account_title')
                        account_title = val.value;
                    if (val.key == 'app_account_url')
                        account_url = val.value;
                    //  控制显示
                    if (val.key == 'app_show_lang' && val.value == "False") {
                        $('switch-lang').hide();
                    }
                    //注意， odoo12，主用户id=2, 加了个 __system__
                    if (val.key == 'app_show_debug' && val.value == "True") {
                        self.show_debug = true;
                    }
                    if (val.key == 'app_show_documentation' && val.value == "False") {
                        $('[data-menu="documentation"]').hide();
                    }
                    if (val.key == 'app_show_documentation_dev' && val.value == "False") {
                        $('[data-menu="documentation_dev"]').hide();
                    }
                    if (val.key == 'app_show_support' && val.value == "False") {
                        $('[data-menu="support"]').hide();
                    }
                    if (val.key == 'app_show_account' && val.value == "False") {
                        $('[data-menu="account"]').hide();
                    }
                    if (val.key == 'app_account_title' && val.value) {
                        $('[data-menu="account"]').html(account_title);
                    }
                    if (val.key == 'app_show_poweredby' && val.value == "False") {
                        $('.o_sub_menu_footer').hide();
                    }
                });
                if (!self.show_debug || !session.is_admin) {
                    $('[data-menu="debug"]').hide();
                    $('[data-menu="debugassets"]').hide();
                    $('[data-menu="quitdebug"]').hide();
                }
            })
        },
        /**
         * @override
         * 由于odoo11 没传ev到事件，所以要重载
         */
        async willStart() {
            await this._super(...arguments);
            var self = this;
            try {
                self.is_manager = await session.user_has_group('base.group_erp_manager');
            } catch {
                self.is_manager = false;
            }
        },
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                //语言切换特殊处理
                self.$el.on('click', 'a[data-lang-menu]', function (ev) {
                    ev.preventDefault();
                    var f = self['_onMenuLang']
                    f.call(self, $(this));
                });
                if (!self.show_debug || !self.is_manager) {
                    setTimeout(function () {
                        $('[data-menu="debug"]').hide();
                        $('[data-menu="debugassets"]').hide();
                        $('[data-menu="quitdebug"]').hide();
                    }, 500)
                }
                // if (self.is_manager) {
                //     //控制debug显示
                //     var mMode = 'normal';
                //     if (window.location.href.indexOf('debug=1') != -1)
                //         mMode = 'debug';
                //     if (window.location.href.indexOf('debug=assets') != -1)
                //         mMode = 'assets';
                //
                //     if (mMode == 'normal')  {
                //         $('[data-menu="debug"]').show();
                //         $('[data-menu="debugassets"]').show();
                //         $('[data-menu="quitdebug"]').hide();
                //     }
                //     if (mMode == 'debug'){
                //         $('[data-menu="debug"]').hide();
                //         $('[data-menu="debugassets"]').show();
                //         $('[data-menu="quitdebug"]').show();
                //     }
                //     if (mMode == 'assets')  {
                //         $('[data-menu="debug"]').show();
                //         $('[data-menu="debugassets"]').hide();
                //         $('[data-menu="quitdebug"]').show();
                //     }
                // }
            });
        },
        _onMenuAccount: function () {
            window.open(account_url, '_blank');
        },
        _onMenuDocumentation: function () {
            window.open(documentation_url, '_blank');
        },
        _onMenuSupport: function () {
            window.open(support_url, '_blank');
        },
        //增加的方法
        _onMenuDebug: function () {
            window.location = $.param.querystring(window.location.href, 'debug=1');
        },
        _onMenuDebugassets: function () {
            window.location = $.param.querystring(window.location.href, 'debug=assets');
        },
        _onMenuQuitdebug: function () {
            window.location = $.param.querystring(window.location.href, 'debug=0');
        },
        _onMenuDocumentation_dev: function () {
            window.open(documentation_dev_url, '_blank');
        },
        _onMenuLang: function (ev) {
            var self = this;
            var lang = ($(ev).data("lang-id"));
            var session = this.getSession();
            return this._rpc({
                model: 'res.users',
                method: 'write',
                args: [session.uid, {'lang': lang}],
            }).then(function (result) {
                self.do_action({
                    type: 'ir.actions.client',
                    res_model: 'res.users',
                    tag: 'reload_context',
                    target: 'current',
                });
            });
        },
    })

});
