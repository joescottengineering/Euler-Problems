# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 19:27:40 2015

@author: JKandFletch
"""

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
def fib(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        

n = 0
num = 0

while num < 10**999:
    n += 1
    num = fib(n)
    
print n
print fib(n-1)
print len(str(fib(n-1)))
print fib(n)
print len(str(fib(n)))