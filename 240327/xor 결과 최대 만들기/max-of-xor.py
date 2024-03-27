# 재귀적으로 m번의 xor 결과 중 최대 값을 찾는 함수
def max_xor(nums, m, idx, cnt, result):
    if cnt == m: return result
    if idx >= len(nums):
        if cnt == m: return result
        else: return -1

    max_result = max(result, max_xor(nums, m, idx + 1, cnt + 1, result ^ nums[idx]), max_xor(nums, m, idx + 1, cnt, result))

    return max_result

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
print(max_xor(nums, m, 0, 0, 0))