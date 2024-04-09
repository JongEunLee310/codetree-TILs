n, m = [int(x) for x in input().split()]
elem = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

d = {}
for e in elem:
    try:
        d[e] += 1
    except:
        d[e] = 1

for n in nums:
    if n in d:
        print(d[n], end=' ')
    else:
        print(0, end=' ')