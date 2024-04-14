import heapq

n, m = [int(x) for x in input().split()]
nums = [-int(x) for x in input().split()]
heapq.heapify(nums)
for _ in range(m):
    heapq.heappush(nums, heapq.heappop(nums) + 1)

print(-nums[0])