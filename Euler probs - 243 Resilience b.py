# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:28:39 2015

@author: JKandFletch
"""


import math
from collections import Counter
import time
import numpy as np

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
        self.a = [1] * limit              # Initialize the primality list of zeroes
        self.a[0] = self.a[1] = 0

        for (i, factor) in enumerate(self.a):
            if factor == 1:
                self.primes.add(i)
                if i*i <= limit:
                    for n in xrange(i*2, limit, i):     # Mark factors non-prime
                        self.a[n] += 1

    def isPrime(self, num):
        if num in self.primes:
            return True
        else:
            return False

    def getPrimes(self):
        return self.primes

    def getComposites(self):
        return self.a


@ memoize
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


def relativePrimes(num, divisors):
    relPrimes = [1] * num
#    print num, list(divisors)
    for divisor in list(divisors):
        i = 1
        while divisor * i < num and divisor**2 < num:
            relPrimes[divisor * i] = 0
            i += 1
#            print relPrimes, num, divisor
    return sum(relPrimes) - 1

min_value = 1
min_num = 0
min_combo = np.array([1])
limit = 100
primes = thePrimes(limit)
the_list = list(primes.getPrimes())
#factors = primes.getComposites()
target = 15499.0/94744.0
#target = 4.0/10.0

num_fact = 8
done = False

while not done:
    combo = np.array(the_list[:num_fact])
    num = np.prod(combo.astype(np.float))
    value = float(relativePrimes(num, combo)) / (num - 1)
    if value < min_value:
        min_value = value
        min_num = num
        min_combo = combo
    if value < target:
        print num
        done = True
        break
    num_fact += 1
    if num_fact > 20:
        done = True
        print 'Wow!'


print min_value, min_num