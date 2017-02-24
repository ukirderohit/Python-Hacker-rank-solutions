noofgames = (int(raw_input()))
score = map(int,raw_input().split())
highscore=score[0]
lowestscore = score[0]
highct = 0
lowct = 0
for sc in score:
    if sc>highscore:
        highscore = sc
        highct += 1
    if sc<lowestscore:
        lowestscore = sc
        lowct += 1
print highct, lowct