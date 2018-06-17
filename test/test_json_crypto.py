
import logging
import pathlib
import unittest

from encrypted_config.crypto import encrypt
from encrypted_config.json_crypto import JSONEncrypter, JSONDecrypter

_LOG = logging.getLogger(__name__)

_HERE = pathlib.Path(__file__).parent


class Tests(unittest.TestCase):

    def test_encrypter_decrypter(self):
        public_key_path = pathlib.Path(_HERE, 'test_id_rsa.pub.pem')
        _LOG.info('using public key: %s', public_key_path)

        private_key_path = pathlib.Path(_HERE, 'test_id_rsa')
        _LOG.info('using private key: %s', private_key_path)

        encrypter = JSONEncrypter(public_key_path)
        decrypter = JSONDecrypter(private_key_path)
        secret = encrypt('my-secret', public_key_path)

        for example in ('""', '"1234"', '[]', '["1234"]', r'{}', r'{"key"}'):
            pass
        for example in ('"secure:{}"'.format(secret), '["1234", "secure:{}"]'.format(secret)):
            pass
