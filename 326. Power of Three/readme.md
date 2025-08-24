#  Power of Three (LeetCode 326)

**Problem Link:** [https://leetcode.com/problems/power-of-three](https://leetcode.com/problems/power-of-three)  

---

## Approach

- First check if n <= 0 and return False (powers of 3 are always positive)
- Use a while loop to repeatedly divide n by 3 as long as it's divisible by 3
- After removing all factors of 3, check if we're left with 1
- If n is a power of 3, dividing by 3 repeatedly should eventually give us 1
- If n has any factors other than 3, the final result won't be 1

---

## Complexity
- **Time:** O(log₃ n). Dividing by 3 until we reach 1
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
