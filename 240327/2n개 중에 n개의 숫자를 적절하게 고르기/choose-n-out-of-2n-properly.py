from sys import maxsize

# 첫번째 그룹을 재귀적으로 만들어 최소 차이를 구하는 함수
def min_diff(nums, n, idx, g):
    if len(g) == n: return get_diff(nums, g)
    if idx >= len(nums):
        if len(g) == n: return get_diff(nums, g)
        else: return maxsize

    min_d = maxsize
    # 현재 인덱스를 포함하는 첫번째 그룹
    g.append(idx)
    d1 = min_diff(nums, n, idx + 1, g)
    g.pop()

    # 현재 인덱스를 포함하지 않는 첫번째 그룹
    d2 = min_diff(nums, n, idx + 1, g)

    min_d = min(min_d, d1, d2)

    return min_d

# 두 그룹 간 원소 합의 차이를 구하는 함수
def get_diff(nums, g1):
    sum_g1 = 0
    for idx in g1:
        sum_g1 += nums[idx]

    # 전체에서 g1의 원소합을 뺀 값이 g2의 원소합이므로 두 그룹의 차이를 구하기 위해 전체합에서 g1를 한 번 더 빼야한다.
    return abs(sum(nums) - sum_g1 * 2)

n = int(input())
nums = [int(x) for x in input().split()]
print(min_diff(nums, n, 0, []))