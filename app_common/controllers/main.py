# -*- coding: utf-8 -*-

import base64
from io import BytesIO
import requests
from math import radians, cos, sin, asin, sqrt

from ..lib.user_agents import parse

from odoo import api, http, SUPERUSER_ID, _
from odoo import http, exceptions
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class AppController(http.Controller):

    def get_image_from_url(self, url):
        if not url:
            return None
        try:
            response = requests.get(url)  # 将这个图片保存在内存
        except Exception as e:
            return None
        # 返回这个图片的base64编码
        return base64.b64encode(BytesIO(response.content).read())

    @http.route('/web/ua/show', auth='public', methods=['GET'])
    def app_ua_show(self):
        # https://github.com/selwin/python-user-agents
        ua_string = request.httprequest.headers.get('User-Agent')
        user_agent = parse(ua_string)
        ua_type = self.get_ua_type()
        ustr = "Request UA: <br/> %s <br/>Parse UA: <br/>%s <br/>UA Type:<br/>%s <br/>" % (ua_string, str(user_agent), ua_type)
        return request.make_response(ustr, [('Content-Type', 'text/html')])
        
    def get_ua_type(self):
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
    
    def app_get_client_ip(request):
        """
        获取请求IP
        """
        ip = ''
        try:
            # HTTP_X_FORWARDED_FOR: 浏览当前页面的用户计算机的网关.
            x_forwarded_for = request.META.get('X-Forwarded-For')
            x_real_ip = request.META.get('X-Real-IP')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            elif x_real_ip:
                # REMOTE_ADDR: 浏览当前页面的用户计算机的ip地址
                ip = x_real_ip
            else:
                ip = request.META.get('REMOTE_ADDR')
        except Exception as e:
            logging.info(_("Request user IP address failed. error msg:{}").format(e))
        return ip

def haversine(lon1, lat1, lon2, lat2):
    # 计算地图上两点的距离
    # in:经度1，纬度1，经度2，纬度2 （十进制度数）
    # out: 距离（米）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000
