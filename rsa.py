#!/usr/bin/env python

import argparse
import logging
import sys

from ciphers.rsa import keygen, cipher


def _translate(cipher_func, key_file, infile, outfile, mode='encrypt'):
    logging.debug('%s: %s %s %s', mode, key_file.name, infile.name,
                  outfile.name)
    cipher_func(key_file, infile, outfile)


def decrypt(args):
    _translate(cipher.decrypt, args.private_key_file, args.infile,
               args.outfile, mode='decrypt')


def encrypt(args):
    _translate(cipher.encrypt, args.public_key_file, args.infile, args.outfile)


def genkeys(args):
    key_file_name = args.key_file_name
    logging.debug('genkeys %s', key_file_name)
    keygen.main(key_file_name)


def parser_args():
    # Create the top-level parser
    parser = argparse.ArgumentParser(prog='rsa', description='Textbook RSA.')
    parser.add_argument('-d', dest='debug', action='store_true',
                        help='print debug information')
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers(title='subcommands')

    # Create generate keys command parser
    genkeys_parser = subparsers.add_parser('genkeys', help='generate keys')
    genkeys_parser.add_argument('key_file_name', nargs='?',
                                default='textbook_rsa')
    genkeys_parser.set_defaults(func=genkeys)

    # Create encrypt command parser
    encrypt_parser = subparsers.add_parser('encrypt')
    encrypt_parser.add_argument('public_key_file',
                                type=argparse.FileType('r'))
    encrypt_parser.add_argument('infile', nargs='?',
                                type=argparse.FileType('r'),
                                default=sys.stdin)
    encrypt_parser.add_argument('outfile', nargs='?',
                                type=argparse.FileType('w'),
                                default=sys.stdout)
    encrypt_parser.set_defaults(func=encrypt)

    # Create decrypt command parser
    decrypt_parser = subparsers.add_parser('decrypt')
    decrypt_parser.add_argument('private_key_file',
                                type=argparse.FileType('r'))
    decrypt_parser.add_argument('infile', nargs='?',
                                type=argparse.FileType('r'),
                                default=sys.stdin)
    decrypt_parser.add_argument('outfile', nargs='?',
                                type=argparse.FileType('w'),
                                default=sys.stdout)
    decrypt_parser.set_defaults(func=decrypt)

    args = parser.parse_args()
    return parser, args


def main():
    parser, args = parser_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.func is None:
        parser.print_help()
        raise SystemExit()

    args.func(args)


if __name__ == '__main__':
    main()
