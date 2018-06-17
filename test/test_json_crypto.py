
import logging
import pathlib
import unittest

from encrypted_config.json_io import str_to_json
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

        for example in (r'{"key": "1234", "secure:key": ""}', r'{"key": "test", "secure:key": ""}'):
            data = str_to_json(example)
            encrypted_data = encrypter.transform(data)
            _LOG.warning('encrypted data: %s', encrypted_data)
            self.assertNotIn('key', encrypted_data)
            self.assertIn('secure:key', encrypted_data)
            self.assertTrue(encrypted_data['secure:key'])
            decrypted_data = decrypter.transform(encrypted_data)
            self.assertIn('key', decrypted_data)
            self.assertEqual(decrypted_data['key'], data['key'])
        for example in ('"secure:{}"'.format(secret), '["1234", "secure:{}"]'.format(secret)):
            data = str_to_json(example)
            decrypted_data = decrypter.transform(data)
            self.assertIn('my-secret', decrypted_data)
