# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:21:40 2015

@author: JKandFletch
"""

import math


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorated_function


@memoize
def isPrime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


total = 1
nextStep = 1
n = 2
ratio = 1.0
numPrimes = 0
numDiags = 1

while ratio > .1:
    for i in range(1, 5):
        nextStep = nextStep + n
        if isPrime(nextStep):
            numPrimes += 1
        numDiags += 1
    ratio = float(numPrimes)/float(numDiags)
    n += 2

print numPrimes, numDiags, n-1
