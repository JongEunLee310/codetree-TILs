# 각 자리에 1 ~ 4인 정수를 넣는 모든 경우의 수 중 최대 결과를 내는 것을 탐색하는 함수
def get_maximum(f, nums, idx):
    if idx == len(nums): return cal(f, nums)

    max_cal = 0
    for i in range(1, 5):
        nums[idx] = i
        max_cal = max(max_cal, get_maximum(f, nums, idx + 1))
    
    return max_cal

# 수식 계산 함수
def cal(f, nums):
    result = 0
    i = 0
    while i < len(f): 
        if i == 0:
            result += nums[ord(f[i]) - ord('a')]
            i += 1
            continue

        if f[i] == '+':
            result += nums[ord(f[i + 1]) - ord('a')]
        elif f[i] == '-':
            result -= nums[ord(f[i + 1]) - ord('a')]
        elif f[i] == '*':
            result *= nums[ord(f[i + 1]) - ord('a')]
        i += 2
    return result

# 변수로 사용되는 알파벳 순으로 가장 뒤에 있는 알파벳 순서만큼 nums 리스트 초기화하는 함수 -> 예) a, b, c 중 c를 골라서 a ~ c까지 리스트 공간을 할당
def init_nums(f):
    max_c = 'a'
    for c in f:
        if not (c == '+' or c == '-' or c == '*'):
            max_c = max(max_c, c)
    nums = [0 for _ in range(ord(max_c) - ord('a') + 1)]
    return nums

f = input()
nums = init_nums(f)
print(get_maximum(f, nums, 0))