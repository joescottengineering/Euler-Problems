# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:58:17 2015

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
def quickFact(num):
    total = 1
    for i in range(num, 0, -1):
        total = total * i

    return total


def choose(n, r):
    result = quickFact(n)/(quickFact(r) * quickFact(n-r))
    return result

result = []
count = 0

for n in range(1, 101):
    for r in range(1, n):
        temp = choose(n, r)
        if temp >= 1000000:
            print temp
            result.append(temp)
            count += 1

print len(result)
print count
