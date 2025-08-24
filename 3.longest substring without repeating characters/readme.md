# Longest Substring Without Repeating Characters (LeetCode 3)

**Problem Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/description](https://leetcode.com/problems/longest-substring-without-repeating-characters/description)  

---

## Approach

- Use the sliding window technique with two pointers (left and right).
- Maintain a set to track unique characters in the current window.
- Expand right as long as characters are unique.
- If a duplicate is found, shrink from the left until the duplicate is removed.
- Update the maximum window length at each step.

---

## Complexity
- **Time:** O(n). Each character is added and removed from the set at most once.
- **Space:** O(min(n,26)). Only 26 characters in English alphabet

---

## Solution
- [Python Solution](./python/solution.py)
