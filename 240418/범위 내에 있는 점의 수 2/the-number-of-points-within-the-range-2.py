N, Q = [int(x) for x in input().split()]
dots = {int(dot) : True for dot in input().split()}

# 누적합을 사용
    # 수평선의 길이를 문제의 최대값인 1000001개로 정의
    # 현재 인덱스까지 놓여있는 점의 개수를 초기화
        # 점이 있다면 1 추가한다.
        # 없으면 이전 인덱스의 값을 그대로 가져온다.
max_len = 1000001
prefix_sum = [0 for _ in range(max_len)]
for i in range(1, max_len):
    prefix_sum[i] = prefix_sum[i - 1] + 1 if i in dots else prefix_sum[i - 1]

for _ in range(Q):
    s, e = [int(x) for x in input().split()]
    print(prefix_sum[e] - prefix_sum[s - 1])