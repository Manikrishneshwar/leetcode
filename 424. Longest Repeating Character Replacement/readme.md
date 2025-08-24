#  Longest Repeating Character Replacement (LeetCode 424)

**Problem Link:** [https://leetcode.com/problems/longest-repeating-character-replacement](https://leetcode.com/problems/longest-repeating-character-replacement)  

---

## Approach (solution.py)

- Use sliding window technique with a frequency map to track character counts
- For each character, update its frequency in the map using explicit if-else check
- Calculate the maximum frequency in the current window by finding max(freq.values())
- The key insight: window size - max_frequency = number of characters that need replacement
- When window_size - max_frequency > k, shrink the window from the left until valid
- Track the maximum valid window size throughout the process

---

## Complexity
- **Time:** O(n). each iteration calls max(freq.values()) which is O(26) for at most 26 letters
- **Space:** O(1). frequency map stores at most 26 characters (constant space)

---

## Approach (optimized.py)

- Use sliding window technique with a frequency map to track character counts
- Maintain maxfreq to track the highest frequency of any character in the current window
- The key insight: window size - maxfreq = number of characters that need replacement
- Expand the window by moving right pointer and updating frequency map
- When window_size - maxfreq > k, shrink the window from the left until valid
- Track the maximum valid window size throughout the process
- A valid window is one where we need at most k replacements to make all characters the same

---

## Complexity
- **Time:** O(n). each character is added and removed from the window at most once
- **Space:** O(1). frequency map stores at most 26 characters (constant space)

---

## Solution
- [Python Solution](./python/solution.py)
- [Python Optimized Solution](./python/optimized.py)