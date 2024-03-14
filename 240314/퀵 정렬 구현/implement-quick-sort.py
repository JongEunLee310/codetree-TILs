def quick_sort(arr, low, high):
  if low < high:
    pos = partition(arr, low, high)

    quick_sort(arr, low, pos - 1)
    quick_sort(arr, pos + 1, high)
    
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

n = int(input())
arr = [int(x) for x in input().split()]
quick_sort(arr, 0, len(arr) - 1)
for n in arr:
  print(n, end=' ')