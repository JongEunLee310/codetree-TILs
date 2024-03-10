from sys import maxsize

n = int(input())
nums = [int(x) for x in input().split()]

fmin, smin, fmin_cnt, smin_cnt = maxsize, maxsize, 0, 0
for num in nums:
    if num < fmin:
        if fmin != maxsize:
            smin = fmin
            smin_cnt = fmin_cnt
        fmin = num
        fmin_cnt = 1
    elif num == fmin:
        fmin_cnt += 1
    elif num > fmin:
        if num < smin:
            smin = num
            smin_cnt = 1
        elif num == smin:
            smin_cnt += 1

if smin_cnt == 1:
    print(nums.index(smin) + 1)
else:
    print(-1)