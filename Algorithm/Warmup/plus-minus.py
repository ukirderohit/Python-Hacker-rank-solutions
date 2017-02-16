#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(float,raw_input().strip().split(' '))
pos=0
neg=0
for i in arr:
    if i==0:
        continue
    if i > 0:
        pos += 1
    else:
        neg += 1
    
print pos,neg
print("{:.6f}\n{:.6f}\n{:.6f}\n").format(pos/n,neg/n,(n-(pos+neg))/n)
        