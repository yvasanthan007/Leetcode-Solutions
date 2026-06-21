# Intuition
Traverse the second string and check if all characters of the first string appear in the same order.

# Approach
1. Use a pointer `i` for string `s`.
2. Traverse string `t`.
3. If the current character in `t` matches `s[i]`, move `i` forward.
4. Continue until the end of `t`.
5. If `i` reaches the length of `s`, then `s` is a subsequence of `t`.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for a in t:
            if i < len(s) and s[i] == a:
                i += 1

        return len(s) == i
