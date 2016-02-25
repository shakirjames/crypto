# Based on  Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

from ..utils import LETTERS, hacker_main

CIPHERTEXT = 'GUVF VF ZL FRPERG ZRFFNTR.'


def hack(message=CIPHERTEXT):
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key % len(LETTERS)
                symbol = LETTERS[num]
            translated = translated + symbol
        print('Key #%s: %s' % (key, translated))


if __name__ == '__main__':
    hacker_main(hack)
