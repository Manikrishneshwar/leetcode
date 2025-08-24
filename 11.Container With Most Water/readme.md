# Container With Most Water (LeetCode 11)

**Problem Link:** [https://leetcode.com/problems/container-with-most-water](https://leetcode.com/problems/container-with-most-water)  

---

## Approach

- Use two pointers (left at start, right at end).
- Compute area = (right - left) * min(height[left], height[right]).
- Track the maximum area found so far.
- Move the pointer corresponding to the smaller height inward, since moving the larger one cannot increase the area.
- Continue until pointers meet.

---

## Complexity
- **Time:** O(n). Each element is considered at most once by left/right.
- **Space:** O(1)
---

## Solution
- [Python Solution](./python/solution.py)
