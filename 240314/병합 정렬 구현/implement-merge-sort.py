def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    l_idx, r_idx = 0, 0

    new_arr = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            new_arr.append(left[l_idx])
            l_idx += 1
        else:
            new_arr.append(right[r_idx])
            r_idx += 1
    
    while l_idx < len(left):
        new_arr.append(left[l_idx])
        l_idx += 1
    
    while r_idx < len(right):
        new_arr.append(right[r_idx])
        r_idx += 1

    return new_arr

n = int(input())
arr = [int(x) for x in input().split()]

sorted_arr = merge_sort(arr)
for n in sorted_arr:
    print(n, end=' ')