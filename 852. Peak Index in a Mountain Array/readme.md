#  Peak Index in a Mountain Array (LeetCode 852)

**Problem Link:** [https://leetcode.com/problems/peak-index-in-a-mountain-array](https://leetcode.com/problems/peak-index-in-a-mountain-array)  

---

## Approach

- Use binary search to find the peak element in the mountain array
- Handle edge case for arrays with only 2 elements
- At each iteration, check if mid is the peak by comparing with both neighbors
- If mid is still on the ascending slope (arr[mid-1] < arr[mid] < arr[mid+1]), move right
- If mid is on the descending slope, move left
- Continue until the peak is found

---

## Complexity
- **Time:** O(log n). eliminate half the search space in each iteration
- **Space:** O(1).  constant space

---

## Solution
- [Python Solution](./python/solution.py)
