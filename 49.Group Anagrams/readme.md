#  Group Anagrams (LeetCode 49)

**Problem Link:** [https://leetcode.com/problems/group-anagrams](https://leetcode.com/problems/group-anagrams)  

---

## Approach

- Use a hashmap to group strings with the same character composition
- For each string, sort its characters to create a unique key for anagrams
- Strings that are anagrams will have the same sorted character sequence
- Group all strings with the same sorted key together in the hashmap
- Return all the grouped values as the final result

---

## Complexity
- **Time:** O(n × k log k). Where n is number of strings, k is average string length (sorting each string takes k log k)
- **Space:** O(n × k). Storing all strings in the hashmap

---

## Solution
- [Python Solution](./python/solution.py)
