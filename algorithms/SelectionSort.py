def selectionSort(arr):
  for i in range(len(arr) - 1):
    min = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    if arr[min] < arr[i]:
      arr[i], arr[min] = arr[min], arr[i]