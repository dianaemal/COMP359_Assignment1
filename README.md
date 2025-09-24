# Assignment 1 – COMP 359  
**Group 7 – Topic:** Creating different merge functions for merge sort (in-place and not in-place)  
**Date:** Sep 23, 2025  

---

## Plan & Logging of Work   
- **Version control:** Git was used to track all contributions. See `plans/git_log.txt`.  
- **Task tracking:** Kanban board used for task assignment and progress. See `plans/kanban_screenshot.png`.  
- **Task split:**  
  - **Diana Emal:** Implemented Working Area Merge and Naive In-Place Merge, handled testing and logging outputs and measured runtime.  
  - **Bilal Ahmad:** Implemented Basic Merge Sort, prepared baseline comparisons and wrote the citations.  
  - **Siddharth Soni:** Implemented Gap Method In-Place Merge and tested performance.  
- All members contributed coding, testing, and documentation.
- All of the merge functions, run_test function, and performance_test function can be found in `All_merge_functions.py`.

---

## Analysis Framework   
We compared four implementations of Merge Sort, analyzing **time complexity and space complexity**:  

| Variant | Time Complexity | Space Complexity |
|---------|----------------|-----------------|
| Basic Merge Sort | O(n log n) | O(n) |
| Working Area Merge Sort | O(n log n) | O(n) (reused) | 
| Naive In-Place Merge Sort | O(n²) worst-case | O(1) | 
| Gap Method In-Place Merge Sort | O(n log² n) | O(1) | 

**Discussion:**  
- Basic Merge Sort is fastest and stable.  
- Working Area Merge Sort reduces repeated allocations but slightly slower.  
- Naive In-Place is very slow on large arrays but memory-efficient.  
- Gap Method In-Place is faster than naive in-place and space-efficient. 

---

## Implementation / Experiment  
- **Diana Emal:** Working Area Merge + Naive In-Place Merge implemented in Python. See `Naive_InPlace.py` 
- **Bilal Ahmad:** Basic Merge Sort implemented in Python, runtime recorded and compared. See `TopDownDesign.py`
- **Siddharth Soni:** Gap Method In-Place Merge implemented in Python, tested on large arrays. See `gapmethodmergesort.py`
- All of the functions were tested on arrays of sizes 10k, 50k, 100k.

**Performance Table (Seconds):**  

| Input Size | Basic | Working Area | Naive In-Place | Gap Method |
|------------|-------|--------------|----------------|------------|
| 10,000     | 0.0107 | 0.0162 | 0.0968 | 0.0569 |
| 50,000     | 0.0567 | 0.0834 | 2.3563 | 0.3763 |
| 100,000    | 0.1291 | 0.1938 | 9.9096 | 0.8528 |
 

---

## Debugging / Testing Code   
- **Methods used:** print statements, assertions, structured test cases.  
- **Example test cases:**  
  - Empty input → `[]`  
  - Single element → `[x]`  
  - Already sorted → unchanged  
  - Reverse sorted → correctly sorted  
  - Random arrays with duplicates → correctly sorted  
- **Logs:** All outputs and runtime results are included in `tests/outputs.log`.  

---

## References / Citations   
- Liu, X. (2013). *AlgoXY: Merge sort implementation in C (mergesort.c)* [Source code]. GitHub. https://github.com/liuxinyu95/AlgoXY/blob/algoxy/sorting/merge-sort/src/mergesort.c  
- GeeksforGeeks. (n.d.). *Merge Sort - Data Structure and Algorithm Tutorials*. GeeksforGeeks. https://www.geeksforgeeks.org/merge-sort/  
- YouTube. (2023). *Merge Sorted Arrays Without Extra Space | 2 Optimal Solution* [Video]. YouTube. https://www.youtube.com/watch?v=n7uwj04E0I4  

---




