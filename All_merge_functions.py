import random
import time
import math

# ========== Variant 1 : Basic Merge Sort ==========
def merge_basic(array, l, mid, r):
    left = array[l: mid] + [float('inf')]
    right = array[mid : r] + [float('inf')]
    i, j = 0, 0
    for k in range(l, r):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

def msort_basic(array, l, r):
    if r - l > 1:
        mid = ( r + l ) // 2
        msort_basic(array, l, mid)
        msort_basic(array, mid, r)
        merge_basic(array, l, mid, r)

# ======== Variant 2 : Working Area Merge Sort ========
def merge_work(array, aux, l , mid, r):
    i, j , k = l, mid, l
    while i < mid and j < r:
        if (array[i] <= array[j]):
            aux[k] = array[i]
            i += 1
        else:
            aux[k] = array[j]
            j += 1
        k += 1
    while i < mid:
        aux[k] = array[i]
        i += 1
        k += 1
    while j < r:
        aux[k] = array[j]
        j += 1
        k += 1
    for i in range(l, r):
        array[i] = aux[i]

def msort_work(array, aux, l, r):
    if r - l > 1:
        mid = ( r + l ) // 2
        msort_work(array, aux, l, mid)
        msort_work(array, aux, mid, r)
        merge_work(array, aux, l, mid, r)

# ======== Variant 3 : Naive In-Place Merge Sort ========
def merge_inplace(array, l, mid, r):
    while l < mid and mid < r:
        if (array[l] <= array[mid]):
            l += 1
        else:
            value = array[mid]
            array[l + 1 : mid + 1] = array[l: mid]
            array[l] = value
            l += 1
            mid += 1

def msort_inplace(array, l, r):
    if r - l > 1:
        mid = ( r + l ) // 2
        msort_inplace(array, l, mid)
        msort_inplace(array, mid, r)
        merge_inplace(array, l, mid, r)

# ========= Variant 4 : In-Place Merge Sort using Gap Method ==========
def inplace_merge_gap(arr, left, mid, right):
    total_len = right - left + 1
    gap = math.ceil(total_len / 2)
    while gap > 0:
        i = left
        j = left + gap
        while j <= right:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        if gap == 1:
            break
        gap = math.ceil(gap / 2)

def gap_merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        gap_merge_sort(arr, left, mid)
        gap_merge_sort(arr, mid + 1, right)
        inplace_merge_gap(arr, left, mid, right)

# ========== Test Cases ==========
def run_tests():
    test_cases = [
        [],                  # Empty array
        [1],                 # Single element
        [2, 1],              # Two elements unsorted
        [1, 2],              # Two elements sorted
        [3, 1, 2],           # Three elements
        [1, 2, 3, 4, 5],     # Already sorted
        [5, 4, 3, 2, 1],     # Reverse sorted
        [1, 2, 2, 1],        # Duplicate elements
        [random.randint(0, 100) for _ in range(10)]  # Random small array
    ]

    for idx, arr in enumerate(test_cases):
        print(f"\n--- Test case {idx + 1}: {arr} ---")
        
        arr_basic = arr.copy()
        msort_basic(arr_basic, 0, len(arr_basic))
        print(f"Basic Merge Sort: {arr_basic}")

        arr_work = arr.copy()
        aux = [0] * len(arr_work)
        msort_work(arr_work, aux, 0, len(arr_work))
        print(f"Working Area Merge Sort: {arr_work}")

        arr_inplace = arr.copy()
        msort_inplace(arr_inplace, 0, len(arr_inplace))
        print(f"Naive In-Place Merge Sort: {arr_inplace}")

        arr_gap = arr.copy()
        if len(arr_gap) > 0:
            gap_merge_sort(arr_gap, 0, len(arr_gap) - 1)
        print(f"Gap Method In-Place Merge Sort: {arr_gap}")

# ========== Performance Test ==========
def performance_test():
    array = [random.randint(0, 1000000) for _ in range(100000)]
    array_copy1 = array.copy()
    array_copy2 = array.copy()
    array_copy3 = array.copy()

    print("\n--- Performance Test ---")

    start_time = time.time()
    msort_basic(array_copy1, 0, len(array_copy1))
    print(f"Basic Merge Sort time: {time.time() - start_time:.6f} s")

    aux = [0] * len(array_copy2)
    start_time = time.time()
    msort_work(array_copy2, aux, 0, len(array_copy2))
    print(f"Working Area Merge Sort time: {time.time() - start_time:.6f} s")

    start_time = time.time()
    msort_inplace(array_copy3, 0, len(array_copy3))
    print(f"Naive In-Place Merge Sort time: {time.time() - start_time:.6f} s")

    array_copy4 = array.copy()
    start_time = time.time()
    gap_merge_sort(array_copy4, 0, len(array_copy4) - 1)
    print(f"Gap Method In-Place Merge Sort time: {time.time() - start_time:.6f} s")

if __name__ == "__main__":
    run_tests()
    performance_test()
