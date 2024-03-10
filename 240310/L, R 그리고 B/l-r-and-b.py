grid = [input() for _ in range(10)]
B, L = [], []
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'B':
            B.append(i)
            B.append(j)
        if grid[i][j] == 'L':
            L.append(i)
            L.append(j)

result = abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1
print(result)