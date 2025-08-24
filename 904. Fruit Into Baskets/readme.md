#  Fruits Into Baskets (LeetCode 904)

**Problem Link:** [https://leetcode.com/problems/fruit-into-baskets](https://leetcode.com/problems/fruit-into-baskets)  

---

## Approach

- Handle base cases for arrays of length 1 and 2 explicitly
- Use sliding window approach to find the longest subarray with at most 2 distinct fruit types
- Maintain a count dictionary to track frequency of each fruit type in the current window
- Start with an initial window of size 2, then expand by moving the right pointer
- When encountering a third fruit type:
    - Shrink the window from the left by removing one fruit type completely
    - Continue shrinking until only one distinct fruit type remains, then add the new fruit
- Track the maximum window size throughout the process

---

## Complexity
- **Time:** O(log n). each element is processed at most twice (once when added, once when removed)
- **Space:** O(1).  count dictionary stores at most 3 fruit types (constant space)

---

## Solution
- [Python Solution](./python/solution.py)
