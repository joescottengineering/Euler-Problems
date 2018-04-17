# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 16:39:12 2015

@author: JKandFletch
"""


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


def genSquares():
    q = 1

    while True:
        yield q**2

        q += 1

primeGen = genPrimes()
maxPrime = primeGen.next()
primes = [maxPrime]
primeSet = set()
primeSet.add(maxPrime)

squareGen = genSquares()
maxSquare = squareGen.next()
squares = [maxSquare]

solved = False
thisNum = 1

while not solved:
    thisNum += 2

    while thisNum > maxPrime:
        maxPrime = primeGen.next()
        primeSet.add(maxPrime)
        primes.append(maxPrime)
    while thisNum > maxSquare:
        maxSquare = squareGen.next()
        squares.append(maxSquare)

    if thisNum not in primeSet:
        gotIt = False
        solved = True
        for prime in primes:
            if gotIt:
                break
            tempSum = 0
            for square in squares:
                tempSum = prime + 2 * square
                if thisNum == tempSum:
                    gotIt = True
                    solved = False
                if gotIt:
                    # print thisNum, prime, square
                    break

print thisNum
