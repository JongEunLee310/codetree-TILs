n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

# 최대값의 제한치 = possible_max, 구간합이 될 수 있는 모든 값(nums 최대값 ~ nums 모든 수의 합)을 비교
for possible_max in range(max(nums), sum(nums) + 1):
    # 입력된 숫자들을 맨 앞부터 파티션을 나누며 계산
    partition = 0
    sec_sum = 0
    for i in range(n):
        if possible_max < sec_sum + nums[i]:
            partition += 1
            sec_sum = nums[i]
        else:
            sec_sum += nums[i]
    # 파티션의 수가 m - 1일 때 최소 최대 구간합을 출력
    if partition <= m - 1:
        print(possible_max)
        break