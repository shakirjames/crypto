#!/usr/bin/python

# Prime Number Sieve
# http://inventwithpython.com/hacking (BSD Licensed)

# Primality Testing with the Rabin-Miller Algorithm
# http://inventwithpython.com/hacking (BSD Licensed)

import logging
import sys
import time

from decimal import Decimal
from functools import partial
from random import randrange

#from .cryptomath import rabin_miller


def rabin_miller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5):  # try to falsify num's primality 5 times
        a = randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:  # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def is_prime_rabin_miller(num, check_low_primes=True):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabin_miller().
    logging.debug('using rabin miller test ...')

    if (num < 2):
        return False  # 0, 1, and negative numbers are not prime

    if check_low_primes:
        logging.debug('checking low primes ...')
        # About 1/3 of the time we can quickly determine if num is not prime
        # by dividing by the first few dozen prime numbers. This is quicker
        # than rabin_miller(), but unlike rabin_miller() is not guaranteed to
        # prove that a number is prime.
        low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        if num in low_primes:
            return True

        # See if any of the low prime numbers can divide num
        for prime in low_primes:
            if (num % prime == 0):
                return False

    # If all else fails, call rabin_miller() to determine if num is a prime.
    return rabin_miller(num)


def is_prime_divide(num):
    # Returns True if num is a prime number, otherwise False.

    # Note: Generally, isPrime() is slower than primeSieve().

    # all numbers less than 2 are not prime
    logging.debug('using divide test...')

    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    sqrt_num = Decimal(num).sqrt()  # use decimal to avoid int OverflowError
    for i in range(2, int(sqrt_num) + 1):
        if num % i == 0:
            return False
    return True


def generate_large_prime(keysize=1024):
    # Return a random prime number of keysize bits in size.
    while True:
        num = randrange(2**(keysize-1), 2**(keysize))
        if is_prime_rabin_miller(num):
            return num


def main():
    method = ('rabin_miller_low_primes', 'rabin_miller', 'divide')
    try:
        method = sys.argv[1]
    except IndexError:
        method = method[0]

    try:
        keysize = int(sys.argv[2])
    except IndexError:
        keysize = 1024

    num = randrange(2**(keysize-1), 2**(keysize))

    logging.info('is_prime: method %s, keysize %s bits', method, keysize)
    logging.debug('num: %s', num)

    if method == 'divide':
        is_prime = is_prime_divide
    elif method == 'rabin_miller':
        is_prime = partial(is_prime_rabin_miller, check_low_primes=False)
    elif method == 'rabin_miller_low_primes':
        is_prime = partial(is_prime_rabin_miller, check_low_primes=True)
    else:
        raise SystemExit('Unknown prime algorithm.')

    start_time = time.time()
    accept = is_prime(num)
    total_time_s = time.time() - start_time
    total_time_ms = round(total_time_s * 1000, 2)

    print('{}'.format(accept))
    print('{} ms'.format(total_time_ms))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
