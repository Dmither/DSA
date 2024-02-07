def quickSort(arr):
  if len(arr) < 2:
    return arr
  pivot = arr[0]
  less = []
  more = []
  for i in arr[1:]:
    if i < pivot:
      less.append(i)
    else:
      more.append(i)
  return quickSort(less) + [pivot] + quickSort(more)

arr = [3, 6, 1, 5, 2, 3]
print(quickSort(arr))
