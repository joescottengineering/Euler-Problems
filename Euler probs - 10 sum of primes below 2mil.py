# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 20:54:38 2015

@author: JKandFletch
"""


limit = 2000000
result= []
startSq = 0
totalAns = 0L

a = [True] * limit              # Initialize the primality list
a[0] = a[1] = False

for (i, isprime) in enumerate(a):
    if isprime:
        result.append(i)
        if i*i <= limit:
            for n in xrange(startSq, limit, i):     # Mark factors non-prime
                a[n] = False

totalAns = sum(result)

#print result
print len(result)
            
print totalAns