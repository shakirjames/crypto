# Ciphers

Based on Sweigart's book [Hacking Secret Ciphers with Python][invent].



## Symmetric ciphers

Encrypt

    $ python3 translate.py caesar --key 3 > encrypted.txt


Decrypt

    $ python3 translate.py caesar --decrypt --key 3 < encrypted.txt


Hack

    $ python3 hack.py caesar

Test

    $ python3 test.py caesar


## Asymmetric ciphers

### Primes

    $ cd ciphers/cryptolib/

Usage

    primes [method] [keysize]

Divide Test

    $ python3 primes.py divide


Rabin Miller Test

    $ cd ciphers/cryptolib/
    $ python3 primes.py rabin_miller


Rabin Miller improved by first checking low primes

    $ python3 primes.py rabin_miller_low_primes 2046


### Textbook RSA

Generate key

    $ rsa genkeys [filename]

Encrypt a message with your public key

    $ python3 rsa.py encrypt pubic_key.txt plaintext_message.txt > ciphertext_message.txt

Decrypt a message with your private key

    $ python3 rsa.py decrypt private_key.txt ciphertext_message.txt


Encrypt and decrypt a message

    $ python3 rsa.py -d encrypt pubic_key.txt < plaintext_message.txt | python3 rsa.py decrypt private_key.txt


[invent]: https://inventwithpython.com/hacking/chapters/
