# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 21:00:06 2015

@author: JKandFletch
"""


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
def quickFact(num):
    total = 1
    for i in range(num, 0, -1):
        total = total * i

    return total


def factorialSum(num):
    result = 0
    for char in str(num):
        result += quickFact(int(char))
    return result

maxSum = 1
maxDigits = 1
results = []


for i in range(2, 12):
    maxSum = i * quickFact(9)
    maxDigits = int('9' * i)
    if maxDigits > maxSum:
        print i

for n in range(3, 10**7):
    if n == factorialSum(n):
        results.append(n)

print results
print sum(results)
