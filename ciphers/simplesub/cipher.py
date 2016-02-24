"""Simple Substitution Cipher"""

# Based on Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)


import logging

from random import shuffle
from ..utils import LETTERS, CipherValueError, cipher_main


def _translate(key, message, is_encrypting=False, letters=LETTERS):
    translated = []
    charsA = letters
    charsB = key

    if not is_encrypting:
        logging.debug('Decrpyting')
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            index = charsA.find(symbol.upper())
            translated_symbol = charsB[index]
            logging.debug('symbol %s', symbol)
            logging.debug('translated_symbol %s', translated_symbol)
            if symbol.isupper():
                translated_symbol = translated_symbol.upper()
            else:
                translated_symbol = translated_symbol.lower()
        else:
            translated_symbol = symbol
        translated.append(translated_symbol)
    return ''.join(translated)


def check_valid_key(key, letters=LETTERS):
    key_list = list(key)
    letters_list = list(letters)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        raise CipherValueError('There is an error in the key or symbol set.')


def decrypt(key, message):
    logging.debug('Encrypting msg %s... with key %s', message[:50], key)
    #check_valid_key(key)  # ignore check for hacker
    return _translate(key, message, is_encrypting=False)


def encrypt(key, message):
    logging.debug('Encrypting msg %s... with key %s', message[:50], key)
    check_valid_key(key)
    return _translate(key, message, is_encrypting=True)


def get_random_key(message, letters=LETTERS):
    key = list(LETTERS)
    shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    cipher_main(encrypt, decrypt, get_random_key)
