#!/usr/bin/python

# test.py Tests ciphers for Hacking Lab (CSCI 533 Network Security)
#
# Based on Transposition Cipher Test
# http://inventwithpython.com/hacking (BSD Licensed)

# Assumes cipher.encrypt(key, message), cipher.decrypt(key, message), and
# cipher.get_random_key(message)

import random
import sys

from ciphers.utils import import_cipher_module


def _test(translate, num_runs=26):
    random.seed(42)
    for i in range(num_runs):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: %s...' % (i+1, message[:50]))

        key = translate.get_random_key(message)
        encrypted = translate.encrypt(key, message)
        if message == encrypted:
            print('Message == encrypted')
            sys.exit()
        decrypted = translate.decrypt(key, encrypted)
        if message != decrypted:
            print('Mistmatch with key %s and message %s' % (key, message))
            print(decrypted)
            sys.exit()
    print('Cipher test passed.')


def main():
    try:
        name = sys.argv[1]
    except IndexError:
        raise SystemExit('Enter cipher module to test.')

    cipher_module = import_cipher_module(name)
    _test(cipher_module)


if __name__ == '__main__':
    main()
