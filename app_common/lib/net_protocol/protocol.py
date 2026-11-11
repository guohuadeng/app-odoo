# -*- coding: utf-8 -*-
"""通用通讯协议工具：签名、防重放、限流。

本包必须保持纯 Python：不 import odoo，供 Odoo 模块与独立进程
（app_stock_srv/hub、app_saas_tunnel/tools、ocn_srv）共用。
"""
import hashlib
import hmac
import threading
import time

NONCE_WINDOW = 60
RATE_WINDOW = 60


def now_ts():
    """当前 Unix 时间戳（秒）。"""
    return int(time.time())


def sha256_hex(data):
    """字符串/字节的 SHA-256 十六进制摘要。"""
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data or b'').hexdigest()


def canonical_message(*parts, body=b''):
    """按 NUL 拼接字段，并追加 body 的 SHA-256 二进制摘要。

    与 app_stock_srv / app_saas_tunnel 既有协议保持一致：
        db \x00 route \x00 login \x00 ts \x00 nonce \x00 sha256(body)
    """
    chunks = []
    for part in parts:
        if isinstance(part, bytes):
            chunks.append(part)
        elif part is None:
            chunks.append(b'')
        else:
            chunks.append(str(part).encode('utf-8'))
    if isinstance(body, str):
        body = body.encode('utf-8')
    chunks.append(hashlib.sha256(body or b'').digest())
    return b'\x00'.join(chunks)


def sign(secret, *parts, body=b''):
    """HMAC-SHA256 签名，返回十六进制字符串。"""
    if isinstance(secret, bytes):
        key = secret
    else:
        key = str(secret or '').encode('utf-8')
    return hmac.new(key, canonical_message(*parts, body=body), hashlib.sha256).hexdigest()


def verify(secret, signature, *parts, body=b''):
    """恒定时间校验签名。"""
    expected = sign(secret, *parts, body=body)
    return hmac.compare_digest(expected, signature or '')


def timestamp_ok(ts, window=NONCE_WINDOW, now=None):
    """时间戳是否在允许窗口内。"""
    try:
        ts = int(ts)
    except (TypeError, ValueError):
        return False
    current = now if now is not None else time.time()
    return abs(current - ts) <= window


def hash_token(token):
    """实例令牌的 SHA-256 摘要；服务端只存摘要。"""
    return sha256_hex(token or '')


def verify_token_hash(token, token_hash):
    """恒定时间校验令牌摘要。"""
    return hmac.compare_digest(hash_token(token), token_hash or '')


class NonceCache(object):
    """线程安全的 nonce 一次性缓存，默认窗口 60 秒。"""

    def __init__(self, window=NONCE_WINDOW):
        self.window = window
        self._seen = {}
        self._lock = threading.Lock()

    def claim(self, nonce):
        """登记 nonce；首次返回 True，重复返回 False。"""
        if not nonce:
            return False
        now = time.time()
        with self._lock:
            for key, seen in list(self._seen.items()):
                if now - seen > self.window * 2:
                    self._seen.pop(key, None)
            if nonce in self._seen:
                return False
            self._seen[nonce] = now
            return True

    def clear(self):
        with self._lock:
            self._seen.clear()


class RateLimiter(object):
    """进程内滑动窗口限流。

    多进程部署时每个进程独立计数；需要全局配额时由网关层再用 Redis/DB 汇总。
    """

    def __init__(self, window=RATE_WINDOW):
        self.window = window
        self._buckets = {}
        self._lock = threading.Lock()

    def allow(self, key, limit):
        """limit <= 0 表示不限；返回 True 表示放行。"""
        if not limit or limit <= 0:
            return True
        now = time.time()
        with self._lock:
            bucket = [t for t in self._buckets.get(key, []) if now - t < self.window]
            if len(bucket) >= limit:
                self._buckets[key] = bucket
                return False
            bucket.append(now)
            self._buckets[key] = bucket
            return True

    def reset(self, key=None):
        with self._lock:
            if key is None:
                self._buckets.clear()
            else:
                self._buckets.pop(key, None)
