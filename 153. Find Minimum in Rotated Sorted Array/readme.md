#  Find Minimum in Rotated Sorted Array (LeetCode 153)

**Problem Link:** [https://leetcode.com/problems/find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)  

---

## Approach

- Use binary search to find the minimum element in the rotated array
- Track the minimum value seen so far using min1 variable
- At each iteration, determine which half contains the minimum:
    - If nums[mid] >= nums[left]: left half is sorted, so minimum in that half is nums[left], then search right half
    - Otherwise: right half is sorted, so update minimum with nums[mid] and search left half
- Continue until the search space is exhausted and return the tracked minimum

---

## Complexity
- **Time:** O(log n). Binary search
- **Space:** O(1). constant space   

---

## Solution
- [Python Solution](./python/solution.py)
