#  Length of Last Word (LeetCode 58)

**Problem Link:** [https://leetcode.com/problems/length-of-last-word](https://leetcode.com/problems/length-of-last-word)  

---

## Approach

- Use the split() method to break the string into a list of words
- Access the last element of the split list using index len(s)-1
- Return the length of that last word
- The split() method automatically handles multiple spaces and leading/trailing whitespace

---

## Complexity
- **Time:** O(n). split() needs to traverse the entire string
- **Space:** O(k). where k is the number of words (split creates a list)

---

## Solution
- [Python Solution](./python/solution.py)
