# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 21:10:46 2015

@author: JKandFletch
"""

def checkDigs(num, denom):
    
    numStr = str(num)
    denStr = str(denom)
    
    if (num > denom) or ('0' in numStr or '0' in denStr) or (num == denom) or ((len(numStr) + len(denStr)) < 4) :
        return False
    
    for i in range(2):
        for j in range(2):

            if (numStr[i] == denStr[j]):
                temp = float(numStr[i-1])/float(denStr[j-1])
                if temp == float(num)/float(denom):
                    return True
    
    return False
    

results = []
numerator = 1
denominator = 1

for n in range(1,100):
    for d in range(1,100):
        if checkDigs(n, d):
            results.append([n,d])
            
print results

for i in range(len(results)):
    numerator *= results[i][0]
    denominator *= results[i][1]
    
print numerator, denominator

for i in range(denominator, 0, -1):
    if numerator % i == 0 and denominator % i == 0:
        print numerator/i, denominator/i
        break
