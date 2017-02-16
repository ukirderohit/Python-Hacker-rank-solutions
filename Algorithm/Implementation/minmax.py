#!/bin/python

import sys


totval = map(int,raw_input().split())

i=0
for val in totval:
    val[i:len(totval)]
    i = i + val
print i