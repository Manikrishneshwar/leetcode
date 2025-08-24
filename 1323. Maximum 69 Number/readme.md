#  Maximum 69 Number (LeetCode 1323)

**Problem Link:** [https://leetcode.com/problems/maximum-69-number](https://leetcode.com/problems/maximum-69-number)  

---

## Approach

- Convert the number to a string to easily access and modify individual digits
- Use find() method to locate the first occurrence of '6' from left to right
- If no '6' is found (returns -1), the number is already maximum, return original number
- Otherwise, replace the first '6' with '9' to maximize the number:
- Convert string to list for mutability
- Replace the character at found index with '9'
- Join back to string and convert to integer
- The key insight: changing the leftmost '6' to '9' gives the maximum possible increase

---

## Complexity
- **Time:** O(n). where n is the number of digits (string operations)
- **Space:** O(n).  creating string and list representations of the number

---

## Solution
- [Python Solution](./python/solution.py)
