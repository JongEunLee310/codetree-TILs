# 재귀적으로 m번의 xor 결과 중 최대 값을 찾는 함수
def max_xor(nums, m, idx, cnt, l):
    if cnt == m: return xor(l)
    if idx >= len(nums):
        if cnt == m: return xor(l)
        else: return -1

    max_result = 0
    # 현재 인덱스의 수를 포함한 xor 결과값
    l.append(nums[idx])
    r1 = max_xor(nums, m, idx + 1, cnt + 1, l)
    l.pop()
    # 현재 인덱스의 수를 제외한 xor 결과값
    r2 = max_xor(nums, m, idx + 1, cnt, l)

    max_result = max(max_result, r1, r2)
    return max_result

# xor 수행 함수
def xor(l):
    result = 0
    for n in l:
        result ^= n
    return result

n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
print(max_xor(nums, m, 0, 0, []))