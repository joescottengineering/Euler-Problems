# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:29:39 2015

@author: JKandFletch
"""


def polyCalc(poly, n):
    if poly == 3:
        return n*(n+1)/2
    elif poly == 4:
        return n**2
    elif poly == 5:
        return n*(3*n-1)/2
    elif poly == 6:
        return n*(2*n-1)
    elif poly == 7:
        return n*(5*n-3)/2
    elif poly == 8:
        return n*(3*n-2)
    else:
        return None

polyList = [[], [], [], [], [], []]
fronts = [{}, {}, {}, {}, {}, {}]
backs = [{}, {}, {}, {}, {}, {}]
nextFront = 10
nextBack = 10

for poly in range(3, 9):
    n = 1
    nextPoly = 1

    while len(str(nextPoly)) < 5:
        if len(str(nextPoly)) == 4:
            nextFront = int(str(nextPoly)[:2])
            nextBack = int(str(nextPoly)[-2:])
            if nextBack >= 10:
                polyList[poly-3].append(nextPoly)
                try:
                    fronts[poly-3][nextFront].append(nextPoly)
                except:
                    fronts[poly-3][nextFront] = [nextPoly]
                try:
                    backs[poly-3][nextBack].append(nextPoly)
                except:
                    backs[poly-3][nextBack] = [nextPoly]
        n += 1
        nextPoly = polyCalc(poly, n)

queue = [[], [], [], [], [], []]
queue[5].extend(polyList[5])
print queue
q_ind = 5
got_em = False
group = [0]*6
next_ind = [5, 0, 1, 2, 3, 4]

while not got_em:
    this_num = queue[q_ind].pop()
    front = int(str(this_num)[:2])
    if q_ind > 0:
        if front in backs[next_ind[q_ind]].keys():
            group[q_ind] = this_num
            print queue
            q_ind = next_ind[q_ind]        
            queue[q_ind].extend(backs[q_ind][front])
    if (q_ind == 0):
        final_num = (int(str(group[5])[-2:]) * 100) + front
        if final_num in polyList[0]:
            got_em = True
            print group
    if len(queue[q_ind]) == 0:
        print queue        
        while not queue[q_ind]:
            q_ind = (q_ind + 1) % 6
    if not queue[5]:
        print 'OOPS!'
        break
