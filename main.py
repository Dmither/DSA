import math
from random import random

from algorithms.SelectionSort import selectionSort
from algorithms.BubbleSort import bubbleSort
from algorithms.InsertionSort import insertionSort
from algorithms.MergeSort import mergeSort

# arr = [2, 5, 1, 8, 3]

arr1 = []
arr2 = []
arr3 = []
arr4 = []
for i in range(9):
  arr1.append(math.ceil(random() * 10))
  arr2.append(math.ceil(random() * 10))
  arr3.append(math.ceil(random() * 10))
  arr4.append(math.ceil(random() * 10))

print(arr1)

selectionSort(arr1)
print(arr1)
print()

print(arr2)
bubbleSort(arr2)
print(arr2)
print()

print(arr3)
insertionSort(arr3)
print(arr3)
print()

print(arr4)
mergeSort(arr4)
print(arr4)
