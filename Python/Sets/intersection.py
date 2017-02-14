a = int(raw_input())
seta = set(map(int,raw_input().split()))
b = int(raw_input())
setb = set(map(int,raw_input().split()))

c =  seta.intersection(setb)
print len(c)