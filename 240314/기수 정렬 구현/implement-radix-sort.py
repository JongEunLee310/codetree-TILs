def radix_sort(k, arr):
    stored_arr = arr
    for pos in range(1, k + 1):
        new_arr = [[] for _ in range(10)]
        for n in stored_arr:
            digit = int(n[-pos]) if len(n) >= pos else 0
            new_arr[digit].append(n)

        stored_arr = []
        for i in range(10):
            for j in range(len(new_arr[i])):
                stored_arr.append(new_arr[i][j])

    return stored_arr
    

n = int(input())
arr = input().split()

max_num = max(arr, key = lambda x : len(x))
k = len(max_num)
sorted_arr = radix_sort(k, arr)
for n in sorted_arr:
    print(n, end=' ')