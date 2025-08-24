#  Largest 3-Same-Digit Number in String (LeetCode 2264)

**Problem Link:** [https://leetcode.com/problems/largest-3-same-digit-number-in-string](https://leetcode.com/problems/largest-3-same-digit-number-in-string)  

---

## Approach

- Use sliding window of size 3 with a frequency array to track digit counts
- Initialize the first window and check if any digit appears 3 times
- Slide the window one position at a time:
- Remove the leftmost digit from frequency count
- Add the new rightmost digit to frequency count
- Check if the new digit appears 3 times in the current window
- Track the largest digit that forms a valid 3-same-digit substring
- Return that digit repeated 3 times, or empty string if none found
- Optimization: return "999" immediately when '9' is found (since it's the maximum possible)

---

## Complexity
- **Time:** O(n). single pass through the string with constant-time window operations
- **Space:** O(1).  frequency array of fixed size 10

---

## Solution
- [Python Solution](./python/mysoln.py)
