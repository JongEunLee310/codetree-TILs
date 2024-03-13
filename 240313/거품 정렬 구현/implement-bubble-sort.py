n = int(input())
arr = [int(x) for x in input().split()]
for i in range(n):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for n in arr:
    print(n, end=' ')