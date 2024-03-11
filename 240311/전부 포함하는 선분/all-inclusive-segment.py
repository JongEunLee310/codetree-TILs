def get_length(lines):
    s = 101
    e = 0
    for i in range(len(lines)):
        s = min(s, lines[i][0])
        e = max(e, lines[i][1])

    return e - s

n = int(input())
lines = [[int(x) for x in input().split()] for i in range(n)]
min_s_lines = sorted(lines, key = lambda x : x[0])
max_e_lines = sorted(lines, key = lambda x : -x[1])

rm_min_s = get_length(min_s_lines[1:])
rm_max_e = get_length(max_e_lines[1:])

result = min(rm_min_s, rm_max_e)
print(result)