#   Trionic Array I (LeetCode 3637)

**Problem Link:** [https://leetcode.com/problems/trionic-array-i](https://leetcode.com/problems/trionic-array-i)  

---

## Approach

- Use state machine approach with three phases to detect trionic pattern (up → down → up)
- Track three boolean flags: inc1 (first increase), dec1 (decrease), inc2 (second increase)
- Phase 1 (!inc1): Continue increasing or transition to decreasing phase
- Phase 2 (!dec1): Continue decreasing or transition to final increasing phase
- Phase 3 (!inc2): Must continue increasing, any decrease/equal invalidates the pattern
- Use left pointer to track the reference element for comparison in current phase
- Return true only if all three phases (inc1, dec1) are completed successfully
- Handle edge cases like arrays too small to form valid trionic pattern

---

## Complexity
- **Time:** O(n). single pass through the array
- **Space:** O(1).  only using boolean flags and pointer variables

---

## Solution
- [Python Solution](./python/solution.py)
