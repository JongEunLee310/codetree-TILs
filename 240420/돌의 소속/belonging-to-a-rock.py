N, Q = [int(x) for x in input().split()]
stones = [0] + [int(input()) for _ in range(N)]

# 누적합을 사용하여 각 그룹마다 해당 숫자까지 그룹에 속한 개수를 초기화
prefix_sum = [[0 for _ in range(N + 1)] for _ in range(4)]
for i in range(1, 4):
    for j in range(1, N + 1):
        # 현재 검사 중인 숫자의 직전 인덱스의 값을 가져온다.
        prefix_sum[i][j] = prefix_sum[i][j - 1]
        # 만일 현재 검사 중인 숫자의 그룹과 현재 그룹이 동일하면 그룹에 속한 숫자의 개수 1 추가
        if stones[j] == i:
            prefix_sum[i][j] += 1

for _ in range(Q):
    s, e = [int(x) for x in input().split()]
    for i in range(1, 4):
        print(prefix_sum[i][e] - prefix_sum[i][s - 1], end=' ')
    print()