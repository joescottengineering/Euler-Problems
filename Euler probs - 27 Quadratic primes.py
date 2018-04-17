# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:58:42 2015

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

    
def quadResult(a, b):
    x = 2
    n = 0
    numberPrimes = 0
    nonPrime = False

    
    while not nonPrime:
        x = n**2 + a * n + b
        if isPrime(x):
            numberPrimes += 1
        else:
            nonPrime = True
        n += 1
    
    return numberPrimes
    
#print quadResult(1,41)
maxNum = 0
returnA = 0
returnB = 0
    
for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        thisCombo = quadResult(i, j)
        if thisCombo > maxNum:
            maxNum = thisCombo
            returnA = i
            returnB = j
            
print maxNum
print returnA, returnB, returnA * returnB