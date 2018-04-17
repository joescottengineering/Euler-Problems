# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 21:23:32 2015
Euler prob 2 - sum of even fibonnaci numbers below 4 million
@author: JKandFletch
"""

result = []

onebefore = 1
lastone = 1
thisone = 0

while thisone < 4000000:
    thisone = lastone + onebefore
    
    if thisone % 2 == 0:
        result.append(thisone)
        
    onebefore = lastone
    lastone = thisone
    
print sum(result)
print result
