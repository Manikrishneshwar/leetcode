#  Binary Search (LeetCode 704)

**Problem Link:** [https://leetcode.com/problems/find-all-anagrams-in-a-string](https://leetcode.com/problems/binary-search)  

---

## Approach

- Use classic binary search algorithm on the sorted array
- Initialize left and right pointers to array boundaries
- In each iteration, calculate the middle index and compare target with nums[mid]
- Based on comparison:
    - If target < nums[mid]: search the left half by setting right = mid - 1
    - If target > nums[mid]: search the right half by setting left = mid + 1
    - If target == nums[mid]: found the target, return mid
- Continue until search space is exhausted, return -1 if not found

---

## Complexity
- **Time:** O(log n). eliminate half the search space in each iteration
- **Space:** O(1).  constant space

---

## Solution
- [Python Solution](./python/solution.py)
