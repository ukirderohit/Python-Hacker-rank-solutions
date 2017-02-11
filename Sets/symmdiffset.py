M = raw_input()
Mval = set(map(int,raw_input().split()))
# print Mval
N = raw_input()
Nval = set(map(int,raw_input().split()))
# print Nval

a = Mval.difference(Nval)
# print a
b = Nval.difference(Mval)
# print b

c = sorted(a.union(b))
# print c

for each in c:
    print each