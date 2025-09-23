#Bilal Ahmad - 300190041

import random
from time import perf_counter

def TDmergeSort(arr):
   if len(arr) <= 1:
       return arr
   mid = len(arr)//2
   left = arr[:mid]
   right = arr[mid:]
   return TDmerge(TDmergeSort(left), TDmergeSort(right))

def TDmerge(a1, a2):
   i, j = 0, 0
   c = []
   while i < len(a1) and j < len(a2):
       if a1[i] < a2[j]:
           c.append(a1[i])
           i += 1
       else:
           c.append(a2[j])
           j += 1
   if i < len(a1):
       c.extend(a1[i:])
   if j < len(a2):
       c.extend(a2[j:])
   return c

t = 0
a = []
while t < 100_000:
   a.append(random.randint(1, 100_000))
   t+=1

td_start = perf_counter()
sortedArray = TDmergeSort(a)
td_end = perf_counter()
print('Top Down elapsed time:', td_end - td_start, ' seconds!')
