grid = [input() for _ in range(10)]
B, L, R = [], [], []
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'B':
            B.append(i)
            B.append(j)
        if grid[i][j] == 'L':
            L.append(i)
            L.append(j)

        if grid[i][j] == 'R':
            R.append(i)
            R.append(j)

result = 0
if B[0] == R[0] and L[0] == R[0]:
    if B[1] < R[1] and R[1] < L[1] or L[1] < R[1] and R[1] < B[1]:  # B, L, R이 일직선 상에 있을 때 R이 B, L 사이에 있으면 우회
        result = abs(B[0] - L[0]) + abs(B[1] - L[1]) + 1
    else:     # B, L, R이 일직선 상에 있을 때 R이 B, L 사이에 없으면 직행
        result = abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1
elif B[1] == R[1] and L[1] == R[1]:
    if B[0] < R[0] and R[0] < L[0] or L[0] < R[0] and R[0] < B[0]:  # B, L, R이 일직선 상에 있을 때 R이 B, L 사이에 있으면 우회
        result = abs(B[0] - L[0]) + abs(B[1] - L[1]) + 1
    else:   # B, L, R이 일직선 상에 있을 때 R이 B, L 사이에 없으면 직행
        result = abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1
else:
    result = abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1
print(result)