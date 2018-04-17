# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 20:05:06 2015

@author: JKandFletch
"""


def genTri():
    tri = 0
    n = 285

    while True:
        tri = n * (n + 1) / 2
        yield tri
        n += 1


def genPent():
    pent = 0
    n = 165

    while True:
        pent = n * (3 * n - 1)/2
        yield pent
        n += 1


def genHex():
    hexa = 0
    n = 144

    while True:
        hexa = n * (2 * n - 1)
        yield hexa
        n += 1


triNum = genTri()
pentNum = genPent()
hexNum = genHex()

three = triNum.next()
five = pentNum.next()
six = hexNum.next()

match = False

while not match:
    while six > five:
        five = pentNum.next()
    while six > three:
        three = triNum.next()
    if six == five and six == three:
        match = True
    else:
        six = hexNum.next()

print three, five, six
