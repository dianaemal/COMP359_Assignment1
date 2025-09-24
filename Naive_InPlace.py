import random
import time

# Diana Emal 
# ========== Merge Sort with Working Area ==========
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
    print(f"Merging: {array[l:mid]} and {array[mid:r]} into {array[l:r]}")
    print(f"Auxiliary array state: {aux[l:r]}")
    for i in range(l, r):
        array[i] = aux[i]

def msort_work(array, aux, l, r):
    if r - l > 1:
        mid = ( r + l ) // 2
        print(f"Dividing: {array[l:r]} into {array[l:mid]} and {array[mid:r]}")
        msort_work(array, aux, l, mid)
        msort_work(array, aux, mid, r)
        merge_work(array, aux, l, mid , r)



# ========== Naive In-Place Merge Sort ==========

def merge_inplace(array, l, mid, r):
    while l < mid and mid < r:

        if (array[l] <= array[mid]):
            l += 1
        else:
            value = array[mid]
            # Shift all elements between l and mid to the right by 1.
            array[l + 1 : mid + 1] = array[l: mid]
            array[l] = value
            l += 1
            mid += 1
        print(f"Merging: {array[l-1:mid]} and {array[mid:r]} into {array[l-1:r]}")


def msort_inplace(array, l, r):
    if r - l > 1:
        mid = ( r + l ) // 2
        print(f"Dividing: {array[l:r]} into {array[l:mid]} and {array[mid:r]}")
        msort_inplace(array, l, mid)
        msort_inplace(array, mid, r)
        merge_inplace(array, l, mid, r)





# ========== Testing the implementations ==========
    
def performance_test():
    array = [random.randint(0, 1000000) for _ in range(100000)]
    array_copy = array.copy()
   
    print("\n--- Using Working Area Merge Sort ---")
  
    aux = [0] * len(array_copy)
    start_time = time.time()
    msort_work(array_copy, aux, 0, len(array_copy))
    end_time = time.time()


    print(f"Time taken: {end_time - start_time:.6f} seconds")

    print("\n--- Using Naive In-Place Merge Sort ---")
  
    start_time = time.time()
    msort_inplace(array_copy, 0, len(array_copy))
    end_time = time.time()  

    print(f"Time taken: {end_time - start_time:.6f} seconds")

def main():
   
    print("Testing Merge Sort with Working Area:\n")
    arr1 = [3, 1, 2]
    aux1 = [0] * len(arr1)
    msort_work(arr1, aux1, 0, len(arr1))
    print( arr1)
    print("\nTesting Naive In-Place Merge Sort:")
    arr2 = [3, 1, 2]
    msort_inplace(arr2, 0, len(arr2))
    print( arr2) 

        
    
   
if __name__ == "__main__":
    main ()