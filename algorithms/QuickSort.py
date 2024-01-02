def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  i += 1
  arr[i], arr[high] = arr[high], arr[i]

  return i

def quickSort(arr, low=0, high=-1):
  if high == -1:
    high = len(arr) - 1
  
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
