def binarySearch(arr, item):
  if len(arr) == 0:
    return -1
  index = len(arr) // 2
  if arr[index] == item:
    return index
  if item < arr[index]:
    return binarySearch(arr[:index], item)
  if arr[index] < item:
    x = binarySearch(arr[index+1:], item)
    if (x > -1):
      return index + 1 + x
  return -1