# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 19:43:35 2015

@author: JKandFletch
"""


import time

start = time.time()

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


def rotStr(string):
    results = []
    stringTemp = string
    for i in range(len(string)):
        stringTemp = stringTemp[-1] + stringTemp[:-1]
        results.append(stringTemp)
    return results

limit = 1000000
primes = genPrimes(limit)
circularList = []

for prime in primes:
    strPrime = str(prime)
    if (len(strPrime) > 1) and (('2' in strPrime) or ('0' in strPrime) or ('4' in strPrime) or ('8' in strPrime) or ('6' in strPrime) or ('5' in strPrime)):
        continue
    else:
        flag = True
        toCheck = rotStr(strPrime)
        for rotation in toCheck:
            if int(rotation) not in primes:
                flag = False
                break
        if flag:
            circularList.append(prime)

print circularList
print len(circularList)
print time.time() - start
