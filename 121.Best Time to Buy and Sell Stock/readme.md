#  Best Time to Buy and Sell Stock (LeetCode 121)

**Problem Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)  

---

## Approach

- Use two pointers approach with left representing the buy day
- Iterate through all prices with index i representing potential sell days
- For each day, check if current price is lower than our buy price:
- If prices[i] < prices[left]: update left to i (found a better buy opportunity)
- Otherwise: calculate profit prices[i] - prices[left] and update maximum profit
- Keep track of the maximum profit seen throughout the iteration
- The key insight: always buy at the lowest price seen so far

---

## Complexity
- **Time:** O(n). Iterate through the array once
- **Space:** O(1). constant space   

---

## Solution
- [Python Solution](./python/solution.py)
