n = int(input())
arr = [int(x) for x in input().split()]

for i in range(1, n):
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j -= 1

for n in arr:
    print(n, end=' ')