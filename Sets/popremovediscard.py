n = input()
s = set(map(int, raw_input().split())) 
N = int(input())
for i in range(N):
    cmd = (raw_input() + " ").split(" ")
    eval('s.' + cmd[0] + '(' + cmd[1] + ')')
print(sum(s))