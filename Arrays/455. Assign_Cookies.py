# Intuition
Give the smallest possible cookie that can satisfy each child. Sort both arrays and use two pointers to match them greedily.

# Approach
1. Sort the greed factors and cookie sizes.
2. Use two pointers: one for children and one for cookies.
3. If the current cookie can satisfy the current child, move to the next child.
4. Always move to the next cookie.
5. The number of satisfied children is the answer.

# Complexity
- Time complexity:
O(n log n + m log m)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i, j = 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i
