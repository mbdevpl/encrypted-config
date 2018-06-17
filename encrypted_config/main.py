
import argparse
import logging
import pathlib

from .json_io import str_to_json, json_to_str, file_to_json
from .json_crypto import encrypt_json, decrypt_json

_LOG = logging.getLogger(__name__)


def parse_args(args):
    """Command-line argument parsing for encrypted_config CLI."""
    parser = argparse.ArgumentParser(
        prog='encrypted_config', description='',
        epilog='Copyright 2018-2019  Mateusz Bysiek  https://mbdevpl.github.io/',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('command', type=str, choices=['encrypt', 'decrypt'])
    parser.add_argument(
        '--key', required=True, metavar='PATH',
        help='path to keyfile (public key if encrypting, private key if decrypting)')

    path_group = parser.add_mutually_exclusive_group(required=True)
    path_group.add_argument('--path', metavar='PATH', help='path to JSON configuration file')
    path_group.add_argument('--json', metavar='JSON', help='inline JSON configuration')

    template_group = parser.add_mutually_exclusive_group()
    template_group.add_argument('--template', metavar='JSON', help='inline JSON template')
    template_group.add_argument('--template-path', metavar='PATH', help='path to JSON template')

    return parser.parse_known_args(args)


def main(args=None):
    """Entry point of encrypted_config CLI."""
    parsed_args, coordinates = parse_args(args)

    _LOG.debug('regular args: %s', parsed_args)
    _LOG.debug('coordinates: %s', coordinates)

    if parsed_args.json is not None:
        data = str_to_json(parsed_args.json)
    elif parsed_args.path is not None:
        data = file_to_json(pathlib.Path(parsed_args.path))
    # _LOG.debug('json: %s', data)

    key_path = pathlib.Path(parsed_args.key)
    # _LOG.debug('key: %s', key_path)

    if parsed_args.command == 'encrypt':
        transformed_data = encrypt_json(data, key_path)
    elif parsed_args.command == 'decrypt':
        transformed_data = decrypt_json(data, key_path)

    # _LOG.debug('transformed json: %s', transformed_data)
    print(json_to_str(transformed_data))
