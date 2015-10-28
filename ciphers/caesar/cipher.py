"""Caesar Cipher"""

# Based on Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import logging

from random import randint
from ..utils import LETTERS, cipher_main


def _decrypt_num(num, key):
    return num - key


def _encrypt_num(num, key):
    return num + key


def _translate(key, message, num_function=_encrypt_num, letters=LETTERS):
    translated = []
    n = len(letters)
    message = message.upper()
    for symbol in message:
        if symbol in letters:
            num = num_function(letters.find(symbol), key) % n
            symbol = letters[num]
        translated.append(symbol)
    return ''.join(translated)


def decrypt(key, message):
    logging.debug('Decrypting msg %s... with key %s', message[:50], key)
    return _translate(int(key), message, num_function=_decrypt_num)


def encrypt(key, message):
    logging.debug('Encrypting msg %s... with key %s', message[:50], key)
    return _translate(int(key), message, num_function=_encrypt_num)


def get_random_key(message, letters=LETTERS):
    return randint(0, len(letters) - 1)


if __name__ == '__main__':
    cipher_main(encrypt, decrypt, get_random_key)
