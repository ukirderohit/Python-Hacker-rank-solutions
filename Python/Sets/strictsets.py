seta = set(map(int, raw_input().split()))
n= int(raw_input())
for _ in range(n):
    setb=set(map(int, raw_input().split()))
    output = (len(seta)>len(setb) and seta.issuperset(setb))
    if output!=True:
        break
print output

