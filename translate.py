#!/usr/bin/python

# translate.py Encrypt and decrypt text with ciphers.
#
# Usage:
# $ python3 translate.py caesar --key 3 > encrypted.txt
# $ python3 translate.py caesar --decrypt --key 3 < encrypted.txt


import argparse
import logging
import sys
import time

from ciphers.utils import import_cipher_module


def parse_args(prog='translate', description='Translator.'):
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-d', dest='debug', action='store_true')
    parser.add_argument('cipher', help='cipher name')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument('--key', help='Key')
    parser.add_argument('--decrypt',  action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    message = args.infile.read()

    cipher = import_cipher_module(args.cipher)
    if not args.key:
        args.key = cipher.get_random_key(message)
        print('Using random key {}'.format(args.key), file=sys.stderr)

    start_time = time.time()
    if not args.decrypt:
        mode = 'encrypt'
        print(cipher.encrypt(args.key, message), file=args.outfile)
    else:
        mode = 'decrypt'
        print(cipher.decrypt(args.key, message), file=args.outfile)
    total_time = round(time.time() - start_time, 2)
    print('{}ion time: {} seconds'.format(mode, total_time), file=sys.stderr)

if __name__ == '__main__':
    main()
