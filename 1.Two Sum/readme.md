# Two Sum (LeetCode 1)

**Problem Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)  

---

## Approach
- Use a hashmap to store numbers and their indices.  
- For each element, check if `target - num` exists in the hashmap.  
- If it does, return the pair of indices.  

---

## Complexity
- **Time:** O(n). Iterate through the numbers only once and 'in' uses constant time for searching in hashmaps
- **Space:** O(n).

---

## Solution
- [Python Solution](./python/solution.py)
