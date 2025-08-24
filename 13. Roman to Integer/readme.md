# Two Sum (LeetCode 13)

**Problem Link:** [https://leetcode.com/problems/roman-to-integer](https://leetcode.com/problems/roman-to-integer)  

---

## Approach

- Use a dictionary to map Roman numerals to integer values.
- Initialize result with the value of the first character.
- Iterate through the string from the second character onward:
- Add the current value to the result.
- If the previous numeral is smaller than the current (e.g., IV or IX), subtract twice the previous value (since it was already added once earlier).
- Update prev each step and return the final result.

---

## Complexity
- **Time:** O(n). Iterate through all characters in the string once.
- **Space:** O(1). Dictionary is fixed size (only 7 Roman numerals).

---

## Solution
- [Python Solution](./python/solution.py)
