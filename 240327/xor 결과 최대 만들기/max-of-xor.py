# 재귀적으로 m번의 xor 결과 중 최대 값을 찾는 함수
def max_xor(nums, m, cnt, result):
    if cnt == m: return result

    max_result = 0
    for i in nums:
        max_result = max(max_result, max_xor(nums, m, cnt + 1, i if result == 0 else result ^ i))
    
    return max_result

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
print(max_xor(nums, m, 0, 0))