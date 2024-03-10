n = int(input())
nums = sorted([int(x) for x in input().split()])

result = 1
if n == 3:      # 숫자가 3개일 때는 모두 곱한 값이 최대값
    for num in nums:
        result *= num
else:
    if nums[-1] == 0:   # 최대값이 0일 경우 0을 제외한 나머지가 음수이므로 곱의 최대값은 0
        result = 0
    elif nums[-1] < 0 or nums[0] >= 0:  # 최대값이 음수일 경우 절대값이 가장 작은 3개의 수를 선택해 곱셈한 겂이 최대값 혹은 최소값이 0이상인 경우 절대값이 가장 큰 3개의 수를 선택해 곱셈한 값이 최대값
        for i in range(-1, -4, -1):
            result *= nums[i]
    else:   # 주어진 수가 음수, 양수가 섞여 있을 경우 음수를 포한한 곱과 제외한 곱 중 최대값이 곱의 최대값
        include_neg = nums[0] * nums[1] * nums[-1]
        not_include_neg = nums[-1] * nums[-2] * nums[-3]
        result = max(include_neg, not_include_neg)
print(result)