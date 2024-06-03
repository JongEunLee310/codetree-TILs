from sys import maxsize

n = int(input())
arr = [int(x) for x in input().split()]

ans, cur = -maxsize, 0
i = 0
while i < n:
    if cur < -arr[i]:
        if i + 1 < n:
            cur = arr[i + 1]
            i += 1
    else:
        cur += arr[i]

    if ans < cur:
        ans = cur

    i += 1

print(ans)