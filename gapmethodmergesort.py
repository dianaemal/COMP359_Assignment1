import math

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
