n = int(input())
line = list(input().split())

result = 0
cur_alpha = ord('A')
for i in range(n):
    cur_idx = line.index(chr(cur_alpha))
    while cur_idx > 0 and line[cur_idx - 1] > line[cur_idx]:
        if line[cur_idx - 1] > line[cur_idx]:
            line[cur_idx - 1], line[cur_idx] = line[cur_idx], line[cur_idx - 1]
            cur_idx -= 1
            result += 1
    cur_alpha += 1

print(result)