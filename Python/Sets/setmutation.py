a = int(raw_input())
seta = set(map(int,raw_input().split()))
n = int(raw_input())

for every in range(n):
    operation = (raw_input() + " ").split(" ")
    temp=set(map(int,raw_input().split()))
    eval("seta.{0}(temp)".format(operation[0]))
    
print sum(seta)