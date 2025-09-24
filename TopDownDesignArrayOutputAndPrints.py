#Bilal Ahmad - 300190041

import random
from time import perf_counter

def TDmergeSort(arr):
   if len(arr) <= 1:
       return arr
   mid = len(arr)//2
   l = arr[:mid]
   r = arr[mid:]
   print(f"Dividing: {arr[0:len(arr)]} into {l} and {r}")
   return TDmerge(TDmergeSort(l), TDmergeSort(r))

def TDmerge(a1, a2):
   i, j = 0, 0
   c = []
   print(f"Merging: {a1[0:len(a1)+1]} and {a2[0:len(a2)+1]} into auxillary Array")
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
   print(f"Auxillary Array State: ", c)
   return c

t = 0
a = [3,2,1]
#while t < 100_000:
   #a.append(random.randint(1, 1_000_000))
   #t+=1

td_start = perf_counter()
sortedArray = TDmergeSort(a)
td_end = perf_counter()
print('Top Down elapsed time:', td_end - td_start, ' seconds!',sortedArray[0:20])
