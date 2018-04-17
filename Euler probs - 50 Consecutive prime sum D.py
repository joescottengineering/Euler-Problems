# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 12:09:06 2015

@author: JKandFletch
"""

import time

init=time.time()

def isPrime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return 0
    return 1

mylist=[]
plist=[]
n=3
s=2

while s<10**6:
    if isPrime(n)==1:
        s+=n
        plist.append(n)
        if isPrime(s)==1:
            mylist.append(s)
    n+=2
maxi=mylist[-1]

print len(plist)

for i in range(len(plist)):
    for j in range(i,len(plist)-1):
        s=sum(plist[i:j+1])
        if isPrime(s)==1:
            maxi=max(maxi,s)

print plist
print mylist
print(maxi,time.time()-init)