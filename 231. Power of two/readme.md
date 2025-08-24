#  Power of Two (LeetCode 231)

**Problem Link:** [https://leetcode.com/problems/power-of-two](https://leetcode.com/problems/power-of-two)  

---

## Approach

- First check if n <= 0 and return False (powers of 2 are always positive)
- Use a while loop to repeatedly divide n by 2 as long as it's divisible by 2
- After removing all factors of 2, check if we're left with 1
- If n is a power of 2, dividing by 2 repeatedly should eventually give us 1
- If n has any odd factors other than 1, the final result won't be 1

---

## Complexity
- **Time:** O(log n). Dividing by 2 until reaching 1
- **Space:** O(1). Constant space   

---

## Solution
- [Python Solution](./python/solution.py)
