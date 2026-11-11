# -*- coding: utf-8 -*-
"""通用通讯协议层。

用法：
    from odoo.addons.app_common.lib.net_protocol import sign, verify, NonceCache

独立进程：
    sys.path.insert(0, '<app_common>/lib')
    from net_protocol import sign, verify, NonceCache
"""
from .protocol import (
    NONCE_WINDOW,
    RATE_WINDOW,
    NonceCache,
    RateLimiter,
    canonical_message,
    hash_token,
    now_ts,
    sha256_hex,
    sign,
    timestamp_ok,
    verify,
    verify_token_hash,
)
from .auth import ClientAuth

__all__ = [
    'NONCE_WINDOW',
    'RATE_WINDOW',
    'NonceCache',
    'RateLimiter',
    'ClientAuth',
    'canonical_message',
    'hash_token',
    'now_ts',
    'sha256_hex',
    'sign',
    'timestamp_ok',
    'verify',
    'verify_token_hash',
]
