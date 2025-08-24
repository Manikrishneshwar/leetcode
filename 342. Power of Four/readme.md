#  Power of Four (LeetCode 342)

**Problem Link:** [https://leetcode.com/problems/power-of-four/description](https://leetcode.com/problems/power-of-four/description)  

---

## Approach

- First check if n <= 0 and return False (powers of 4 are always positive)
- Use a while loop to repeatedly divide n by 4 as long as it's divisible by 4
- After removing all factors of 4, check if we're left with 1
- If n is a power of 4, dividing by 4 repeatedly should eventually give us 1
- If n has any factors other than 4, the final result won't be 1

---

## Complexity
- **Time:** O(log4 n). Dividing by 4 until we reach 1
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
