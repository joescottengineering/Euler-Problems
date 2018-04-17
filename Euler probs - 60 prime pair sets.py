# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 19:42:08 2015

@author: JKandFletch
"""


import itertools


def genPrimes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


#def checkSoln(listStr, *primeSet):
#    for 

primeGen = genPrimes()
primeSet = set()
primes = []
setSize = 4
solved = False

for i in range(500):
    maxPrime = str(primeGen.next())
    primeSet.add(maxPrime)
    primes.append(maxPrime)
    print maxPrime

while not solved:
    thisSet = list(itertools.permutations(primes, setSize - 1))
    solved = True
    for combo in thisSet:
        thisCombo = list(combo)
        thisCombo.append(maxPrime)
#        print thisCombo
        checkSet = list(itertools.permutations(thisCombo, 2))
        if maxPrime == '673':
            print thisCombo
        for num in checkSet:
            testNum = num[0] + num[1]
            if testNum not in primeSet:
                solved = False
                break
    if solved:
        print thisCombo
        print 'Hooray!!'
        break
    else:
        maxPrime = str(primeGen.next())
        primeSet.add(maxPrime)
        primes.append(maxPrime)

    if int(maxPrime) > 700:
        solved = True
        print 'Whoops!!'
