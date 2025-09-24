#Siddharth Soni
def next_gap(g):
    """Return ceil(g/2) using integers."""
    return 0 if g <= 1 else (g // 2) + (g % 2)

def inplace_merge_gap(arr, left, right, *, debug=True):
    """
    Gap-method in-place merge for arr[left..right].
    Treats the whole slice as one block; compares elements gap apart,
    swapping when out of order, then shrinks the gap until 1.
    """
    n = right - left + 1
    gap = next_gap(n)

    if debug:
        print(f"\nMERGE slice [{left}:{right}] len={n} start_gap={gap}  -> {arr[left:right+1]}")

    while gap > 0:
        if debug:
            print(f"  pass with gap={gap}")
        i, j = left, left + gap
        while j <= right:
            if arr[i] > arr[j]:
             
                left_val, right_val = arr[i], arr[j]
                arr[i], arr[j] = arr[j], arr[i]
                if debug:
                    print(f"    swap arr[{i}]={left_val} with arr[{j}]={right_val} -> {arr[left:right+1]}")
            i += 1
            j += 1
        gap = next_gap(gap)

    if debug:
        print(f"END MERGE [{left}:{right}] -> {arr[left:right+1]}")

def gap_merge_sort(arr, left=0, right=None, *, debug=True):
    """
    Top-down merge sort; merges each level using the gap method (in-place).
   
    """
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    gap_merge_sort(arr, left, mid, debug=debug)
    gap_merge_sort(arr, mid + 1, right, debug=debug)
    inplace_merge_gap(arr, left, right, debug=debug)

# Example
a = [9, 8, 2, 6, 5, 10]
gap_merge_sort(a)   
print("\nFINAL:", a)            

