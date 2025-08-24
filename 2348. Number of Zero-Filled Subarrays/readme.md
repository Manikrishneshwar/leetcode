#   Number of Zero-Filled Subarrays (LeetCode 2264)

**Problem Link:** [https://leetcode.com/problems/number-of-zero-filled-subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays)  

---

## Approach

- Use two pointers to identify contiguous segments of zeros
- For each contiguous segment of zeros with length n, the number of possible subarrays is n*(n+1)/2
- Track segments using left and right pointers:
    - When encountering zeros, extend the right pointer
    - When encountering non-zero elements, calculate subarrays for the current zero segment
    - Reset pointers to start tracking the next potential zero segment
- Handle the edge case where the array ends with a zero segment
- Use helper function calc(n) to compute the subarray count formula

---

## Complexity
- **Time:** O(n). single pass through the array
- **Space:** O(1).  only using pointer variables and result counter

---

## Solution
- [Python Solution](./python/solution.py)
