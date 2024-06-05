import heapq

n = int(input())
arr = [int(x) for x in input().split()]

# 힙을 사용해서 남은 숫자 중 가장 작은 2개를 골려 합쳐 최소 비용을 계산한다.
heapq.heapify(arr)

cost = 0
# 남은 숫자가 1개가 될 때까지 반복
while len(arr) > 1:
    # n1, n2는 남은 숫자 중 가장 작은 두 수
    n1 = heapq.heappop(arr)
    n2 = heapq.heappop(arr)

    # n3는 n1, n2의 합
        # n3를 cost에 더함
        # n3를 heap에 삽입
    n3 = n1 + n2
    cost += n3
    heapq.heappush(arr, n3)

print(cost)