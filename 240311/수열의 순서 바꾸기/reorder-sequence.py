N = int(input())
nums = [int(x) for x in input().split()]
check = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i >= nums[i] - 1:
        check[nums[i]] = nums[i] - 1
    elif i < nums[i] - 1:
        check[nums[i]] = 1

result = 0
for i in range(N, -1, -1):
    result += check[i]
    if i > 1 and check[i] > 1:
        break

print(result)