def in_range(l1, l2):
    return l1[0] <= l2[0] <= l1[1] or l1[0] <= l2[1] <= l1[1] or l2[0] <= l1[0] <= l2[1] or l2[0] <= l1[1] <= l2[1]

n = int(input())
lines = [[int(x) for x in input().split()] for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if not in_range(lines[i], lines[j]):
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] == 0: dp[i] = 1

print(max(dp))