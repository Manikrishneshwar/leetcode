#  Find Peak Element (LeetCode 162)

**Problem Link:** [https://leetcode.com/problems/find-peak-element](https://leetcode.com/problems/find-peak-element)  

---

## Approach

- Use binary search to find a peak element efficiently
- Handle edge cases: single element, first element as peak, last element as peak
- In the main binary search loop:
    - Check if mid is a peak by comparing with both neighbors
    - If mid is a peak, return it
    - Otherwise, move toward the side that has a higher neighbor (guarantees finding a peak)

---

## Complexity
- **Time:** O(log n). Binary search
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
