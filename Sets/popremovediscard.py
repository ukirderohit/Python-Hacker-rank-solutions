n = int(raw_input())
s = set(map(int, raw_input().split()))
c = int(raw_input())

for i in range(c):
    command = input().split()
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))