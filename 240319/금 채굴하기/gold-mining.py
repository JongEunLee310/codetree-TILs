def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]

# k를 기준으로 완점 탐색
max_profit_gold = 0
for k in range(n):
    cost = 1 if k == 0 else k * k + (k + 1) * (k + 1)
    for i in range(n):
        for j in range(n):
            gold = 0
            for a in range(i - k, i + k + 1):
                for b in range(j - k, j + k + 1):
                    if in_range(a, b, n, n) and abs(i - a) + abs(j - b) <= k and grid[a][b] == 1:
                        gold += 1
            if gold * m >= cost:
                max_profit_gold = max(max_profit_gold, gold)

print(max_profit_gold)