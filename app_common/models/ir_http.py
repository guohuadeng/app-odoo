# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        result['ua_type'] = self.get_ua_type()
        return result

    def get_ua_type(self):
        return get_ua_type()

def get_ua_type():
    ua = request.httprequest.headers.get('User-Agent')
    # 临时用 agent 处理，后续要前端中正确处理或者都从后台来
    # 微信浏览器
    #  MicroMessenger: Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv)
    # AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120
    # MQQBrowser/6.2 TBS/045525 Mobile Safari/537.36 MMWEBID/3135 MicroMessenger/8.0.2.1860(0x2800023B) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64
    # 微信浏览器，开发工具，网页 iphone
    # ,Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
    # wechatdevtools/1.03.2011120 MicroMessenger/7.0.4 Language/zh_CN webview/16178807094901773
    # webdebugger port/27772 token/b91f4a234b918f4e2a5d1a835a09c31e

    # 微信小程序
    # MicroMessenger: Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv)
    # AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2767 MMWEBSDK/20210302 Mobile Safari/537.36 MMWEBID/6689 MicroMessenger/8.0.2.1860(0x2800023B) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64
    # MiniProgramEnv/android
    # 微信浏览器，开发工具，小程序，iphone
    # Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
    # wechatdevtools/1.03.2011120 MicroMessenger/7.0.4 Language/zh_CN webview/
    # 微信内，iphone web
    # Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148
    # MicroMessenger/8.0.3(0x1800032a) NetType/WIFI Language/zh_CN
    # 安卓app,h5
    # ELE-AL00(Android/10) (cn.erpapp.o20sticks.App/13.20.12.09) Weex/0.26.0 1080x2265
    
    # web 表示普通浏览器，后续更深入处理
    utype = 'web'
    # todo: 引入现成 py lib，处理企业微信
    if 'MicroMessenger' in ua and 'webdebugger' not in ua and ('MiniProgramEnv' in ua or 'wechatdevtools' in ua):
        # 微信小程序及开发者工具
        utype = 'wxapp'
    elif 'MicroMessenger' in ua:
        # 微信浏览器
        utype = 'wxweb'
    elif 'cn.erpapp.o20sticks.App' in ua:
        # 安卓app
        utype = 'native_android'
    # _logger.warning('=========get ua %s,%s' % (utype, ua))
    return utype
