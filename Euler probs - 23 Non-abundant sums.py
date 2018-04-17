# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 19:48:21 2015

@author: JKandFletch
"""

import math

limit = 28123

def isAbundant(primes, n):
    if n in primes:
        return False
    divisors = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            if i**2 == n:
                 divisors.append(i)               
            else:
                divisors.append(i)
                divisors.append(n/i)
    
    if sum(divisors) > n:
        return True
    else:
        return False
        
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
                    
primes = genPrimes(limit)
abundants = []
abundantSums = [False]*limit
total = 0

for n in range(1,limit+1):
    if isAbundant(primes,n):
        abundants.append(n)

#print abundants

for i, val in enumerate(abundants):    
    for val2 in abundants[i:]:
        if val + val2 >= limit:
            break
        else:
            abundantSums[val+val2] = True
            #print i, val, val2
        
#print abundantSums

for i, num in enumerate(abundantSums):
    if not num:
        total += i

print total

#for i, num in reversed(list(enumerate(abundantSums))):
#    if num:
#        continue
#    else:
#        print i
#        break