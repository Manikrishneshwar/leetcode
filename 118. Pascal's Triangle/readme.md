#  Pascal's Triangle (LeetCode 118)

**Problem Link:** [https://leetcode.com/problems/pascals-triangle](https://leetcode.com/problems/pascals-triangle)  

---

## Approach

- Handle base cases for numRows = 1 and numRows = 2 explicitly
- Initialize result with the first two rows: [[1], [1,1]]
- For each subsequent row (starting from row 3):
- Create a temporary array of size (i+1) filled with 1s (handles edge elements)
- Fill the middle elements using Pascal's triangle property: temp[j] = res[i-1][j-1] + res[i-1][j]
- Each element is the sum of the two elements directly above it from the previous row
- Append each completed row to the result

---

## Complexity
- **Time:** O(numRows²). Generating numRows rows, where row i has (i+1) elements
- **Space:** O(numRows²). Storing the entire triangle in the result.

---

## Solution
- [Python Solution](./python/solution.py)
