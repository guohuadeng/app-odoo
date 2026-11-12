# -*- coding: utf-8 -*-
"""net_protocol 纯 Python 自测。

运行：
    python -m unittest discover -s app_common/lib -p 'test_*.py'
"""
import unittest

from net_protocol import (
    NonceCache,
    RateLimiter,
    hash_token,
    sign,
    timestamp_ok,
    verify,
    verify_token_hash,
)


class NetProtocolTest(unittest.TestCase):

    def test_sign_legacy_vector(self):
        """与改造前 app_stock_srv / app_saas_tunnel 的内联签名逐字节一致。"""
        import hashlib
        import hmac
        body = b'{"hello": "world"}'
        expected = hmac.new(
            b'secret',
            b'\x00'.join([
                b'db1', b'stock', b'admin', b'1762340000', b'nonce1',
                hashlib.sha256(body).digest(),
            ]),
            hashlib.sha256,
        ).hexdigest()
        self.assertEqual(
            sign('secret', 'db1', 'stock', 'admin', 1762340000, 'nonce1', body=body),
            expected,
        )

    def test_sign_verify_roundtrip(self):
        body = b'{"hello": "world"}'
        sig = sign('secret', 'db1', 'stock', 'admin', 1762340000, 'nonce1', body=body)
        self.assertTrue(verify('secret', sig, 'db1', 'stock', 'admin', 1762340000,
                               'nonce1', body=body))
        self.assertFalse(verify('wrong', sig, 'db1', 'stock', 'admin', 1762340000,
                                'nonce1', body=body))
        self.assertFalse(verify('secret', sig, 'db2', 'stock', 'admin', 1762340000,
                                'nonce1', body=body))

    def test_sign_body_changes(self):
        a = sign('secret', 'db1', 'route', 'admin', 1, 'n', body=b'a')
        b = sign('secret', 'db1', 'route', 'admin', 1, 'n', body=b'b')
        self.assertNotEqual(a, b)

    def test_timestamp_window(self):
        self.assertTrue(timestamp_ok(1000, window=60, now=1030))
        self.assertFalse(timestamp_ok(1000, window=60, now=1061))
        self.assertFalse(timestamp_ok('bad', window=60, now=1000))

    def test_nonce_replay(self):
        cache = NonceCache(window=60)
        self.assertTrue(cache.claim('n1'))
        self.assertFalse(cache.claim('n1'))
        self.assertTrue(cache.claim('n2'))
        self.assertFalse(cache.claim(''))

    def test_rate_limiter(self):
        limiter = RateLimiter(window=60)
        self.assertTrue(limiter.allow('k', 2))
        self.assertTrue(limiter.allow('k', 2))
        self.assertFalse(limiter.allow('k', 2))
        self.assertTrue(limiter.allow('k', 0))
        self.assertTrue(limiter.allow('other', 2))

    def test_token_hash(self):
        token = 'plain-token'
        digest = hash_token(token)
        self.assertTrue(verify_token_hash(token, digest))
        self.assertFalse(verify_token_hash('other', digest))


if __name__ == '__main__':
    unittest.main()
