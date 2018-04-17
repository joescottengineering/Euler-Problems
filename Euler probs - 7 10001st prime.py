# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:06:17 2015

@author: JKandFletch
"""

primes = []
n = 3

while len(primes) < 10001:
    flag = True
    for element in primes:
        if (n % element == 0) and (element != 1):
            flag = False
            break
    if flag:
        primes.append(n)
        #print n
    n += 1
    
print max(primes)
print len(primes)