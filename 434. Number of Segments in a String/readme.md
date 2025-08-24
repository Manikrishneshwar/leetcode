#  Number of Segments in a String (LeetCode 434)

**Problem Link:** [https://leetcode.com/problems/number-of-segments-in-a-string/description](https://leetcode.com/problems/number-of-segments-in-a-string/description)  

---

## Approach

- Use the built-in split() method to break the string into segments
- split() without arguments automatically splits on any whitespace (spaces, tabs, newlines)
- It handles multiple consecutive spaces and leading/trailing whitespace automatically
- Count the number of segments by taking the length of the resulting list
- Empty strings and strings with only whitespace will return 0 segments correctly

---

## Complexity
- **Time:** O(n). split() needs to traverse the entire string once
- **Space:** O(k). where k is the number of segments (creates a list of segments)

---

## Solution
- [Python Solution](./python/solution.py)
