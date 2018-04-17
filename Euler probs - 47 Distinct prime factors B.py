# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:27:54 2015

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


@memoize
def getDivisors(num):
    divisors = Counter()
    tempCnt = Counter()
    if isPrime(num):
        divisors[num] += 1
        return divisors
    else:
        for i in range(2, int(math.sqrt(num))+1):  # search for prime factors
            if num % i == 0 and isPrime(i):
                divisors[i] += 1
                tempCnt = getDivisors(num / i)
                divisors.update(tempCnt)
                break   # stop looking after prime factor found - recursion! :)
    return divisors

fourFound = False
numFour = 0
n = 2*3*5*7

while not fourFound:
    divisorList = getDivisors(n)
    if len(divisorList) == 4:
        numFour += 1
    else:
        numFour = 0

    if numFour == 4:
        fourFound = True
    else:
        n += 1

#for i in range(-3, 1, 1):
#    print n + i, getDivisors(n + i)
print n - 3
print time.time() - start
