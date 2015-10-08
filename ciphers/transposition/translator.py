"""Transposition Cipher"""

# Based on Transposition Cipher Encryption and Transposition Cipher Dencryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math
import logging

from random import randint
from ..utils import cipher_main


def decrypt(key, message):
    logging.debug('Decrypting msg %s... with key %s', message[:50], key)
    key = int(key)
    num_cols = math.ceil(len(message) / key)
    num_rows = key
    num_shaded = (num_cols * num_rows) - len(message)

    plaintext = [''] * num_cols
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if ((col == num_cols) or
                (col == num_cols - 1 and row >= num_rows - num_shaded)):
            col = 0
            row += 1
    return ''. join(plaintext)


def encrypt(key, message):
    logging.debug('Encrypting msg %s... with key %s', message[:50], key)
    key = int(key)
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def get_random_key(message):
    return randint(1, len(message))


if __name__ == '__main__':
    cipher_main()
