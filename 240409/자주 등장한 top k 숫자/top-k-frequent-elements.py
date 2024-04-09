n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}
for num in nums:
    try:
        d[num] += 1
    except:
        d[num] = 1

sorted_num = sorted(d.items(), key = lambda x : [x[1], x[0]], reverse=True)
for i in range(k):
    print(sorted_num[i][0], end=' ')