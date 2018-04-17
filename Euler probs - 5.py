# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:44:30 2015

@author: JKandFletch
"""

result = {}
answer = 1

for A in range(2,21):
    tempA = A    
    for B in range(2,21):
       countB = 0
       
       while (tempA > 1) and (tempA % B == 0):
           countB += 1
           tempA = tempA/B
       
       #print 'A = ' + str(tempA) + ', B = ' + str(B) + ', Count = ' + str(countB)

       if countB > 0:
            if B in result:
                if countB > result[B]:
                    result[B] = countB
            else:
                result[B] = countB

print result

for item in result:
    print str(item) + ', ' + str(result[item])    
    answer = (item ** result[item]) * answer
    print answer
    
print answer
