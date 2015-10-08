# Based on  Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
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
    main()
