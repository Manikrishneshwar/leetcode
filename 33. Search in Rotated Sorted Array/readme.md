#  Search in Rotated Sorted Array (LeetCode 33)

**Problem Link:** [https://leetcode.com/problems/search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array)  

---

## Approach

- Use binary search with modifications to handle the rotation
- Find the mid point and check if it equals target
- Determine which half of the array is properly sorted:
- If nums[left] <= nums[mid]: left half is sorted. Otherwise: right half is sorted
- For the sorted half, check if target lies within its range using normal binary search logic
- For the unsorted half, recursively apply the same logic
- Continue until target is found or search space is exhausted

---

## Complexity
- **Time:** O(log n). Binary search is log n.
- **Space:** O(1).only few variables used.

---

## Solution
- [Python Solution](./python/solution.py)
