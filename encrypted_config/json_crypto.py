"""Decrypting JSON."""

import pathlib
import typing as t

import rsa

from .json_transform import JSONTransformer
from .crypto import prepare_public_key, encrypt, prepare_private_key, decrypt


class JSONEncrypter(JSONTransformer):

    """Encrypt JSON."""

    def __init__(self, public_key: t.Union[pathlib.Path, str, rsa.PublicKey], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._public_key = prepare_public_key(public_key)  # type: rsa.PublicKey

    def transform_dict(self, data: dict) -> dict:
        raise NotImplementedError()

    def transform_list(self, data: list) -> list:
        raise NotImplementedError()

    def transform_str(self, data: list) -> list:
        raise NotImplementedError()


class JSONDecrypter(JSONTransformer):

    """Decrypt JSON."""

    def __init__(self, private_key: t.Union[pathlib.Path, str, rsa.PublicKey], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._private_key = prepare_private_key(private_key)  # type: rsa.PrivateKey

    def transform_dict(self, data: dict) -> dict:
        data = super().transform_dict(data)
        transformed = type(data)()
        for key, value in data.items():
            if key.startswith('secure:'):
                transformed[key[7:]] = decrypt(value, self._private_key)
            else:
                transformed[key] = value
        return transformed

    def transform_list(self, data: list) -> list:
        data = super().transform_list(data)
        transformed = type(data)()
        for value in data:
            if value.startswith('secure:'):
                transformed.append(decrypt(value[7:], self._private_key))
            else:
                transformed.append(value)
        return transformed

    def transform_str(self, data: str) -> str:
        if data.startswith('secure:'):
            return decrypt(data[7:], self._private_key)
        return data
