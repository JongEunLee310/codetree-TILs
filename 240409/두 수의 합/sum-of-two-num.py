n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}.fromkeys(nums, 0)

cnt = 0
for i in range(n):
    # t는 현재 숫자가 k가 되기 위한 숫자를 의미
    t = k - nums[i]
    # t가 d에 있다면 cnt에 현재 인덱스까지 카운트한 t의 개수를 더해준다.
    if t in d:
       cnt += d[t]

    # 현재 숫자가 d에 있을 때 1 추가, 없으면 1로 초기화
    if nums[i] in d:
        d[nums[i]] += 1
 
print(cnt)