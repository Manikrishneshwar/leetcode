#  Minimum Size Subarray Sum (LeetCode 209)

**Problem Link:** [https://leetcode.com/problems/minimum-size-subarray-sum](https://leetcode.com/problems/minimum-size-subarray-sum)  

---

## Approach

- Use sliding window technique with two pointers (left and i as right)
- Expand the window by moving the right pointer and adding elements to the running sum
- When sum becomes greater than or equal to target:
    - Record the current window size i-left+1
    - Update the minimum length seen so far
    - Shrink the window from the left until sum drops below target
- Continue until all elements are processed

---

## Complexity
- **Time:** O(n). right pointer visits each element only once (each element is added or removed once)
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
