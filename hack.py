#!/usr/bin/python

# hack.py Hack ciphers
#
# Assumes hackers.cipher.main()
import sys

from ciphers.utils import import_cipher_module


def main():
    try:
        name = sys.argv[1]
    except IndexError:
        raise SystemExit('Enter cipher module to test.')

    cipher = import_cipher_module(name, module_name='hacker')
    cipher.main()


if __name__ == '__main__':
    main()
