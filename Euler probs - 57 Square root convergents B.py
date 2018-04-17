# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 09:19:10 2015

@author: JKandFletch
"""

results = []
numLarge = 0
numer = 3
denom = 2
iterations = 1000

for i in range(1,iterations):
    results.append((numer, denom))
    oldDenom = denom
    denom = numer + denom
    numer = oldDenom + denom
    if len(str(numer)) > len(str(denom)):
        numLarge += 1

print results
print numLarge
