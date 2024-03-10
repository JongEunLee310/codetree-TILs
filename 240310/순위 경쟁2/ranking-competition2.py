def is_change(stu_score, stu, s, honor):
    result = False
    stu_idx = ord(stu) - ord('A')
    stu_score[stu_idx] += s
    max_score = max(stu_score)
    for i in range(len(stu_score)):
        if stu_score[i] == max_score:
            if not honor[i]:
                honor[i] = chr(i + ord('A'))
                result = True
        else:
            if honor[i]:
                honor[i] = False
                result = True
            
    return stu_score, honor, result            
    
n = int(input())
score = [input().split() for _ in range(n)]
for i in range(n):
    score[i][1] = int(score[i][1])

result = 0
honor = ['A', 'B']
stu_score = [0, 0]
for stu, s in score:
    stu_score, honor, changed = is_change(stu_score, stu, s, honor)
    if changed:
        result += 1

print(result)