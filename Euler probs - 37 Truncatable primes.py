# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 20:59:29 2015

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


def checkTruncRtoL(num):
    numStr = str(num)

    if isPrime(num):
        if len(numStr) == 1:
            return True
        else:
            return checkTruncRtoL(int(numStr[:-1]))

    return False


def checkTruncLtoR(num):
    numStr = str(num)

    if isPrime(num):
        if len(numStr) == 1:
            return True
        else:
            return checkTruncLtoR(int(numStr[1:]))

    return False


def checkcandidate(numAsString):
    acceptableNums = '1379'
    acceptableStarts = '23579'
    if numAsString[0] in acceptableStarts:
        for char in numAsString[1:]:
            if char not in acceptableNums:
                return False
        return True
    return False

truncPrimes = []
n = 11

while len(truncPrimes) < 11:
    numberScreen = str(n)
    if checkcandidate(numberScreen):
        if checkTruncLtoR(n) and checkTruncRtoL(n):
            truncPrimes.append(n)
    n += 1

print truncPrimes
print sum(truncPrimes)

            