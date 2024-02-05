import math
from random import random

from algorithms.SelectionSort import selectionSort
from algorithms.BubbleSort import bubbleSort
from algorithms.InsertionSort import insertionSort
from algorithms.MergeSort import mergeSort
from algorithms.QuickSort import quickSort

R1 = 3
R2 = 8
U = 18
tm = 3.7

t = tm * 60
R = R1 + R2

I = U / R
Isq = I**2
Q1 = Isq * R1 * t
print(round(Q1 / 1000, 1))
Q2 = Isq * R2 * t
print(round(Q2 / 1000, 1))

U1 = U / R * R1
U2 = U / R * R2
Q1 = U1 * I * t
print(round(Q1 / 1000, 1))
Q2 = U2 * I * t
print(round(Q2 / 1000, 1))

Q1 = (U1 ** 2) / R1 * t
print(round(Q1 / 1000, 1))
Q2 = (U2 ** 2) / R2 * t
print(round(Q2 / 1000, 1))