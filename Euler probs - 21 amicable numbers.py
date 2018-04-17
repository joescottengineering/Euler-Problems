# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:35:30 2015

@author: JKandFletch
"""
import math


def getDivisorSum(primes, n):
    if n in primes:
        return 1
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i**2 == n:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)

    return sum(divisors)


def genPrimes(limit):
    primes = []
    a = [True] * limit              # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            if i*i <= limit:
                for n in xrange(0, limit, i):     # Mark factors non-prime
                    a[n] = False

    return primes

limit = 10000

primes = genPrimes(limit)
divisorSums = {}
amicableNums = []

for i in range(2, limit+1):
    divisorSums[i] = getDivisorSum(primes, i)

for key in divisorSums:
    mate = divisorSums[key]
    if mate in divisorSums and divisorSums[mate] == key and mate != key:
        amicableNums.append(key)
        print key, mate

print amicableNums
print sum(amicableNums)
