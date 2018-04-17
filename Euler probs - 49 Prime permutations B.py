# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 10:50:02 2015

@author: JKandFletch
"""


def gen4digPrimes(limit):
    primes = []
    a = [True] * limit              # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            if (len(str(i)) == 4):
                primes.append(i)
            if i*i <= limit:
                for n in xrange(0, limit, i):     # Mark factors non-prime
                    a[n] = False

    return primes


def sortedDigits(num):
    digits = []
    for digit in str(num):
        digits.append(int(digit))
    digits.sort()
    return tuple(digits)

digitPrimes = {}
primes = gen4digPrimes(10000)
differences = {}

for prime in primes:
    theseDigits = sortedDigits(prime)
    if theseDigits in digitPrimes.keys():
        digitPrimes[theseDigits].append(prime)
    else:
        digitPrimes[theseDigits] = [prime]

print digitPrimes[(1, 4, 7, 8)]


setLen = len(digitPrimes[(1, 4, 7, 8)])

for i in range(setLen-1, 1, -1):
    for j in range(i-1, -1, -1):
        value1 = digitPrimes[(1, 4, 7, 8)][i]
        value2 = digitPrimes[(1, 4, 7, 8)][j]
        difference = value1 - value2
        print value1, value2, difference
        if difference in differences:
            #print value1, value2, differences[difference]
            if (value1 in differences[difference]) or \
                    (value2 in differences[difference]):
                print 'match' + str(value1) + str(value2) + \
                    str(differences[difference])
            differences[difference].append(value1)
            differences[difference].append(value2)
#                    print differences[difference]
        else:
            differences[difference] = [value1, value2]
