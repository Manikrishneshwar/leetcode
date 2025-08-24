#  Search Insert Position (LeetCode 35)

**Problem Link:** [https://leetcode.com/problems/search-insert-position/description](https://leetcode.com/problems/search-insert-position/description)  

---

## Approach

- Use binary search to find the target or its insertion position
- Standard binary search: compare target with mid element and adjust left/right pointers
- If target is found during search, return the index immediately
- After the loop ends, determine insertion position based on the final mid value and target comparison

---

## Complexity
- **Time:** O(log n). Binary search is  log n.
- **Space:** O(1). Only few variables used.

---

## Solution
- [Python Solution](./python/solution.py)
