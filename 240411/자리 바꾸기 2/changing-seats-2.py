N, K = [int(x) for x in input().split()]
c_loc = [[int(x) for x in input().split()] for _ in range(K)]

# 1 ~ N번까지의 자리를 리스트로 정의하고 각 인덱스를 [번호, 빈 set]으로 초기화
loc = [[i, set([i])] for i in range(N + 1)]

# K분 동안 자리를 바꾸는 시뮬레이션을 진행
for _ in range(3):
    for i in range(K):
        l1, l2 = c_loc[i]
        # l1, l2에 해당하는 set에 옮겨갈 위치를 추가
        loc[l1][1].add(l2)
        loc[l2][1].add(l1)

        # loc 리스트에서 l1의 set과 l2의 set 위치를 swap
        loc[l1], loc[l2] = loc[l2], loc[l1]

# loc 리스트의 1 ~ N번까지 앉게된 자리 출력
loc.sort(key = lambda x : x[0])
for i in range(1, N + 1):
    print(len(loc[i][1]))