# -*- coding: utf-8 -*-

import base64
from io import BytesIO
import requests

from odoo import api, http, SUPERUSER_ID, _

class ImageController(http.Controller):

    def get_image_from_url(self, url):
        if not url:
            return None
        try:
            response = requests.get(url)  # 将这个图片保存在内存
        except Exception as e:
            return None
        # 返回这个图片的base64编码
        return base64.b64encode(BytesIO(response.content).read())
