#  Maximum Subarray (LeetCode 53)

**Problem Link:** [https://leetcode.com/problems/maximum-subarray](https://leetcode.com/problems/maximum-subarray)  

---

## Approach

- Use Kadane's Algorithm to find the maximum sum subarray in linear time
- Initialize both currentsum and maxsum to the first element
- For each subsequent element, decide whether to:
- Extend the current subarray: currentsum + nums[i]
- Start fresh from current element: nums[i]
- Choose whichever gives a larger sum (this is the key insight of Kadane's algorithm)
- Keep track of the maximum sum seen so far and update it at each step

---

## Complexity
- **Time:** O(n). Single pass through the array
- **Space:** O(1). Only using two variables to track current and maximum sums.

---

## Solution
- [Python Solution](./python/solution.py)
