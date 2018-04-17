# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 19:38:41 2015

@author: JKandFletch
"""

import math

def genTriangle():
    n = 1
    tri = 0
    
    while True:
        tri = tri + n
        yield tri
        n += 1

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
    
numDiv = 1
tempTri = 1
divisors = {}
triNumgen = genTriangle()
for i in range(20):
    triNumgen.next()

primeGen = genPrimes()
primes = [primeGen.next()]

while numDiv < 500:
   
   triStart = tempTri = triNumgen.next()
   numDiv = 1
   
   while max(primes) < triStart:
       primes.append(primeGen.next())

   
   for n in primes:
       if n**2 > triStart:
           break
       num = 1
       while tempTri % n == 0:
           num += 1
           tempTri /= n
       numDiv *= num
       if num == 1:
           break
   
   if numDiv > 300:
       print triStart, numDiv
       
print triStart