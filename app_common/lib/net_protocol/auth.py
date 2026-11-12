# -*- coding: utf-8 -*-
"""通用实例鉴权缓存。

服务端（hub/网关）不保存明文实例密钥，只从内部接口拉取摘要并缓存；
请求到来时用恒定时间比较校验。纯 Python，不 import odoo。
"""
import json
import logging
import threading
import time
import urllib.request

from .protocol import hash_token, verify_token_hash

_logger = logging.getLogger(__name__)


class ClientAuth(object):
    """实例鉴权缓存。

    内部接口返回格式（兼容多种键名）：
        {"clients": [
            {"key": "inst_1", "db": "prod", "secret_hash": "...", "enabled": true}
        ]}
    也兼容 key 为 hub_key / instance_id / client_id 的记录。
    """

    def __init__(self, clients_url, internal_token, refresh_seconds=60,
                 headers=None, timeout=10, logger=None):
        self.clients_url = (clients_url or '').rstrip('/')
        self.internal_token = internal_token or ''
        self.refresh_seconds = refresh_seconds
        self.headers = dict(headers or {})
        self.timeout = timeout
        self.logger = logger or _logger
        self._clients = {}
        self._lock = threading.Lock()
        self._last_refresh = 0.0

    def _fetch(self):
        req = urllib.request.Request(self.clients_url)
        if self.internal_token:
            req.add_header('X-Internal-Token', self.internal_token)
        for key, value in self.headers.items():
            req.add_header(key, value)
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            raw = resp.read().decode('utf-8') or '{}'
        data = json.loads(raw)
        if isinstance(data, dict):
            rows = data.get('clients') or []
        else:
            rows = data or []
        mapping = {}
        for item in rows:
            if not isinstance(item, dict):
                continue
            key = (item.get('key') or item.get('hub_key')
                   or item.get('instance_id') or item.get('client_id'))
            if not key:
                continue
            mapping[key] = {
                'db': item.get('db') or item.get('database') or '',
                'secret_hash': item.get('secret_hash') or '',
                'enabled': bool(item.get('enabled', True)),
            }
        return mapping

    def refresh(self, force=False):
        now = time.time()
        if not force and now - self._last_refresh < self.refresh_seconds:
            return
        try:
            mapping = self._fetch()
            with self._lock:
                self._clients = mapping
            self._last_refresh = now
            self.logger.info('clients refreshed: %d entries', len(mapping))
        except Exception as exc:
            # 失败也退避，避免每个连接都打内部接口
            self._last_refresh = now
            self.logger.warning('clients refresh failed: %s', exc)

    def get(self, key):
        self.refresh()
        with self._lock:
            return self._clients.get(key)

    def is_enabled(self, key):
        info = self.get(key)
        return bool(info and info.get('enabled'))

    def verify(self, key, token, db=None):
        info = self.get(key)
        if not info or not info.get('enabled'):
            return False
        if db and info.get('db') and db != info['db']:
            return False
        return verify_token_hash(token, info.get('secret_hash') or '')

    def token_hash(self, token):
        return hash_token(token)
