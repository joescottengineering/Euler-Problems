# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:05:30 2015

@author: JKandFletch
"""


from collections import OrderedDict

scores = {50: ['DB'], 25: ['B']}
mults = ['S', 'D', 'T']
checkouts = []
outs = OrderedDict([(50, 'DB')])
limit = 99

for i in range(20, 0, -1):
    for mult in range(1, 4):
        this_score = i*mult
        this_score_name = mults[mult-1] + str(i)
        try:
            scores[this_score].append(this_score_name)
        except:
            scores[this_score] = [this_score_name]
        if mult == 2:
            outs[this_score] = this_score_name

throws = list(scores.keys())
throws.sort()

for out in outs.keys():
    this_out = [outs[out]]
    checkouts.append((out, this_out))
    for n, second_throw in enumerate(throws):
        total2 = out + second_throw
        if total2 <= limit:
            for m, second in enumerate(scores[second_throw]):
                temp = this_out[:]
                temp.insert(0, second)
                checkouts.append((total2, temp))
                for third_throw in throws[n:]:
                    total3 = total2 + third_throw
                    if total3 <= limit:
                        if second_throw == third_throw:
                            for third in scores[third_throw][m:]:
                                temp3 = temp[:]
                                temp3.insert(0, third)
                                checkouts.append((total3, temp3))
                        else:
                            for third in scores[third_throw]:
                                temp3 = temp[:]
                                temp3.insert(0, third)
                                checkouts.append((total3, temp3))
                    else:
                        break
        else:
            break


print len(checkouts)

#for solution in checkouts:
#    if solution[0] == 54:
#        print solution