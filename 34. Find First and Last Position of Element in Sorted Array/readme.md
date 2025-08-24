#  Find First and Last Position of Element in Sorted Array (LeetCode 34)

**Problem Link:** [https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)  

---

## Approach

- Use two binary searches to find first and last occurrences separately
- Create a helper function binarySearch with a bias parameter:
    - When bias = True: search for the leftmost occurrence (continue searching left even after finding target)
    - When bias = False: search for the rightmost occurrence (continue searching right even after finding target)
- When target is found, store the index but continue searching in the appropriate direction
- Call the helper function twice: once for first position, once for last position
- Return both results as a list

---

## Complexity
- **Time:** O(log n). Two Binary searches is still log n.
- **Space:** O(1). Only few variables used and no recursion.

---

## Solution
- [Python Solution](./python/solution.py)
