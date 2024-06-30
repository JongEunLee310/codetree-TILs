# 이진탐색을 사용해서 입력된 숫자의 위치를 탐색
def binary_search(nums, tgt):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == tgt:
            return mid + 1

        if nums[mid] > tgt:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

for _ in range(m):
    print(binary_search(nums, int(input())))