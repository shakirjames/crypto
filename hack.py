#!/usr/bin/python

# hack.py Hack ciphers
#
# Assumes hackers.cipher.main()
import sys
import argparse
import logging

from ciphers.utils import import_cipher_module


def parse_args(prog='hacker', description='Hacker.'):
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-d', dest='debug', action='store_true')
    parser.add_argument('cipher', help='cipher hacker name')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'))
    return parser.parse_args()


def main():
    args = parse_args()
    cipher_name = args.cipher
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    hacker = import_cipher_module(cipher_name, module_name='hacker')
    if args.infile:
        hacker.hack(args.infile.read())
    else:
        hacker.hack()

if __name__ == '__main__':
    main()
