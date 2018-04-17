# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:20:54 2015

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

def isPandigit(a, b, c):
    check = '123456789'
    
    thisNum = ''.join(sorted(str(a) + str(b) + str(c)))

    if thisNum == check:
        return True
    else:
        return False
        
def getDivisorPairs(n):
    divisors = [[1,n]]
    
    if isPrime(n):
        return divisors
    
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            if i**2 == n:
                 divisors.append([i, i])               
            else:
                divisors.append([i, n/i])
    
    return divisors

results = []
products = []

for n in range(100000):
    if isPrime(n):
        continue
    else:
        pairs = getDivisorPairs(n)
        for pair in pairs:
            if isPandigit(pair[0], pair[1], n):
                results.append([pair[0], pair[1], n])
                if n not in products:
                    products.append(n)

print results
print products
print sum(products)