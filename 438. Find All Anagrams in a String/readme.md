#  Find All Anagrams in a String (LeetCode 438)

**Problem Link:** [https://leetcode.com/problems/find-all-anagrams-in-a-string](https://leetcode.com/problems/find-all-anagrams-in-a-string)  

---

## Approach

- Use sliding window technique with frequency counting to find anagram matches
- Create frequency maps for pattern p and current window in string s
- Initialize both frequency dictionaries with all lowercase letters set to 0
- Build the initial window of size len(p) and populate its frequency map
- Slide the window through the rest of string s:
    - Remove the leftmost character from window frequency
    - Add the new rightmost character to window frequency
    - Compare window frequency with pattern frequency
- If frequencies match exactly, the current window is an anagram of p

---

## Complexity
- **Time:** O(n). each character in s is processed once
- **Space:** O(1).  two fixed-size dictionaries of 26 characters each

---

## Solution
- [Python Solution](./python/solution.py)
