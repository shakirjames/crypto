"""Caesar Cipher"""

# Based on Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import logging
from random import randint, sample, shuffle

from ..utils import cipher_main, LETTERS


def _decrypt_num(num, key):
    return num - key  # subtract if decrypting


def _encrypt_num(num, key):
    return num + key  # add if encrypting


def _translate(key, message, num_function=_encrypt_num, letters=LETTERS):
    translated = []  # stores the encrypted/decrypted message string

    key_index = 0
    key = key.upper()
    n = len(letters)
    for symbol in message:  # loop through each character in message
        num = letters.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            num = num_function(num, letters.find(key[key_index])) % n
            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                symbol = letters[num]
            elif symbol.islower():
                symbol = letters[num].lower()
            # move to the next letter in the key
            key_index = (key_index + 1) % len(key)

        # The symbol was not in LETTERS, so add it to translated as is.
        translated.append(symbol)
    return ''.join(translated)


def decrypt(key, message):
    logging.debug('Encrypting msg %s... with key %s', message[:50], key)
    return _translate(key, message, num_function=_decrypt_num)


def encrypt(key, message):
    logging.debug('Decrypting msg %s... with key %s', message[:50], key)
    return _translate(key, message, num_function=_encrypt_num)


def get_random_key(message, letters=LETTERS):
    key = list(letters)
    shuffle(key)
    k = randint(1, len(letters))
    return ''.join(sample(key, k))


if __name__ == '__main__':
    cipher_main()
