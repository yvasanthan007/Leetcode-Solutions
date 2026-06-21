# Intuition
Count the frequency of characters in both strings. The extra character in `t` will have a different frequency.

# Approach
1. Create a hash map to store character frequencies from `s`.
2. Traverse `s` and increase the count of each character.
3. Traverse `t` and decrease the count of each character.
4. Find the character whose frequency becomes `-1`.
5. Return that character.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            freq[ch] = freq.get(ch, 0) - 1

        for ch in freq:
            if freq[ch] == -1:
                return ch
