def radix_sort(k, arr):
    result = []
    for pos in range(1, k + 1):
        new_arr = [[] for _ in range(10)]
        for n in arr:
            digit = int(n[-pos]) if len(n) >= pos else 0
            new_arr[digit].append(n)
        
        stored_arr = []
        for i in range(10):
            for j in range(len(new_arr[i])):
                stored_arr.append(new_arr[i][j])

        result = stored_arr

    return result
    

n = int(input())
arr = input().split()

max_num = max(arr)
k = len(max_num)
sorted_arr = radix_sort(k, arr)
for n in sorted_arr:
    print(n, end=' ')