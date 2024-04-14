from sortedcontainers import SortedSet

n, m = [int(x) for x in input().split()]
nums = SortedSet([int(x) for x in input().split()])
query = [int(x) for x in input().split()]

for i in range(m):
    lower_bound = nums.bisect_left(query[i])
    # 질의하는 숫자보다 같거나 큰 최초의 인덱스를 찾았을 때
        # 해당 인덱스의 수가 쿼리하는 수보다 클 경우 인덱스를 1 감소
            # 큰 숫자의 경우에 최초로 큰 숫자이므로 이전 인덱스는 질의하는 숫자보다 작기 때문
            # 1 감소한 인덱스가 0보다 작을 경우 -1 출력
    # 질의하는 숫자와 탐색한 인덱스의 해당하는 숫자가 같을 때
        # 해당 인덱스의 숫자를 출력하고 제거
    # 질의하는 숫자가 수열의 모든 숫자보다 클 때
        # bisect_left를 사용하면 가장 마지막 인덱스보다 1만큼 큰 값이 반환되므로 인덱스 1 감소
    if lower_bound < len(nums) and nums[lower_bound] > query[i] or lower_bound == len(nums):
        lower_bound -= 1

    if lower_bound < 0:
        print(-1)
    else:
        print(nums[lower_bound])
        nums.remove(nums[lower_bound])