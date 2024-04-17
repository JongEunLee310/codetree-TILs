n, k = [int(x) for x in input().split()]
nums = [0] + [int(x) for x in input().split()]

prefix_sum = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]

cnt = 0
i, j = 0, 0
while i < n + 1:
    if prefix_sum[i] - prefix_sum[j] < k:
        i += 1
    elif prefix_sum[i] - prefix_sum[j] == k:
        cnt += 1
        i += 1
    else:
        j += 1
print(cnt)