n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}.fromkeys(nums, 0)

# 첫번째 숫자를 먼저 선택한 후 두번째 숫자와 세번째 숫자의 합이 k - 첫번째 숫자가 되는 모든 쌍을 찾아서 더한다.
cnt = 0
for i in range(n):
    t1 = k - nums[i]
    for j in range(i + 1, n):
        t2 = t1 - nums[j]

        # t2(세번째 숫자)가 있다면 이전 인덱스까지 찾은 t2의 쌍 개수를 cnt에 추가
        if t2 in d:
            cnt += d[t2]
    
    # nums[i](첫번째 숫자)가 d에 있다면 현재까지 조합 개수 1 추가
    if nums[i] in d:
        d[nums[i]] += 1

print(cnt)