def is_consecutive(a, b):
    return abs(a - b) == 1

p = sorted([int(x) for x in input().split()])
is_con = 0
for i in range(2):
    if is_consecutive(p[i], p[i + 1]):
        is_con += 1

result = 0
if is_con != 2:
    result = max(p[2] - p[1], p[1] - p[0]) - 1

print(result)