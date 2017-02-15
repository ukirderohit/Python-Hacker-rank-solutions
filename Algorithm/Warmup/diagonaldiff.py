#!/bin/python

import sys


n = int(raw_input().strip())
a = []
sa = 0
ass = 0
for i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    sa=sa + a[i][i]
    ass = ass + a[i][-i-1]
print abs(sa-ass)
