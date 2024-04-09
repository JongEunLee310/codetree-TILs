n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}
for i in range(n):
    try:
        d[nums[i]][i] = True
    except:
        d[nums[i]] = {i : True}


cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if k - nums[i] in d and j in d[k - nums[i]]:
            cnt += 1
            
print(cnt)