#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
su=0
for val in range(0,len(arr)):
    su = su + arr[val]
    
print su