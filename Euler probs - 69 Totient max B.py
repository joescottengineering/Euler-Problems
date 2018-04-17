# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 21:51:55 2015

@author: JKandFletch
"""


import math
from collections import Counter
import time

start = time.time()


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function


class thePrimes(object):

    def __init__(self, limit):

        self.primes = set()
        a = [True] * limit              # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                self.primes.add(i)
                if i*i <= limit:
                    for n in xrange(0, limit, i):     # Mark factors non-prime
                        a[n] = False

    def isPrime(self, num):
        if num in self.primes:
            return True
        else:
            return False


def getDivisors(num, primes):
    divisors = Counter()
    tempCnt = Counter()
    if primes.isPrime(num):
        divisors[num] += 1
        return divisors
    else:
        for i in range(2, int(math.sqrt(num))+1):  # search for prime factors
            if num % i == 0 and primes.isPrime(i):
                divisors[i] += 1
                tempCnt = getDivisors(num / i, primes)
                divisors.update(tempCnt)
                break   # stop looking after prime factor found - recursion! :)
    return divisors


def relativePrimes(num, primes):
    relPrimes = [1] * num
    divisors = getDivisors(num, primes)

    for divisor in divisors:
        i = 1
        while divisor * i < num:
            relPrimes[divisor * i] = 0
            i += 1
    return sum(relPrimes) - 1

maxResult = 0
maxNum = 0
limit = 1000001
primes = thePrimes(limit)

for i in range(2, limit + 1):
    if primes.isPrime(i):
        continue
    target = i / float(relativePrimes(i, primes))
#    print i, relativePrimes(i, primes), target
    if target > maxResult:
        maxResult = target
        maxNum = i

print maxNum, maxResult
