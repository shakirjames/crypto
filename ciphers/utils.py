import argparse
import logging
import sys

from argparse import ArgumentParser
from importlib import import_module
from os import path


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class CipherNameError(NameError):
    pass


class CipherValueError(ValueError):
    pass


def import_cipher_module(cipher_name, module_name='cipher'):
    cipher_module_name = 'ciphers.{0}.{1}'.format(cipher_name, module_name)
    try:
        return import_module(cipher_module_name)
    except AttributeError:
        raise CipherNameError('Unknown cipher module.')


def parse_args(prog='cipher', description='Cipher.'):
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-d', dest='debug', action='store_true')
    parser.add_argument('message', help='Message to translate')
    parser.add_argument('--decrypt', action='store_true')
    parser.add_argument('--key')
    return parser.parse_args()


def get_filepath(filename, dirname='data'):
    basepath = path.dirname(__file__)
    return path.abspath(path.join(basepath, '..', dirname, filename))


def cipher_main(encrypt, decrypt, get_random_key):
    args = parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if not args.key:
        args.key = get_random_key(args.message)
        print('Using random key {}'.format(args.key))
    if not args.decrypt:
        print(encrypt(args.key, args.message))
    else:
        print(decrypt(args.key, args.message))
