from collections import Counter
size = int(raw_input())
ul = map(int,raw_input().split())
for k,v in Counter(ul).iteritems():
    if v!=size:
        print k

