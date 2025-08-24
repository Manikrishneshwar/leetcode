#  Move Zeroes (LeetCode 283)

**Problem Link:** [https://leetcode.com/problems/move-zeroes](https://leetcode.com/problems/move-zeroes)  

---

## Approach

- Use two pointers technique with left and right pointers
- left pointer tracks the position where the next non-zero element should be placed
- right pointer iterates through all elements in the array
- When right finds a non-zero element:
    - Swap the elements at left and right positions
    - Move left pointer forward to maintain the boundary of non-zero elements
- This ensures all non-zero elements move to the front while maintaining their relative order
- Zeros naturally end up at the end after all swaps

---

## Complexity
- **Time:** O(n). Single array pass
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
