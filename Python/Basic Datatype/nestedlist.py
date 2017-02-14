students=[]
nam=[]
scor=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
    scor.append(score)
    nam.append(name)
# print scor
# scor = list(scor)
scor.sort()
print scor
secmin = 0
for i in range(len(scor)):
    if scor[i]!=scor[i+1]:
        secmin=scor[i+1]
        break
# print nam.sort()
print secmin

students.sort()
nam.sort
for i in range(len(students)):
    for j in range(2):
        if students[i][j]==secmin:
            print nam[i]
print students

