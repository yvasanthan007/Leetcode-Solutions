# Intuition
Two strings are anagrams if they contain the same characters with the same frequencies.

# Approach
1. If the lengths are different, return `False`.
2. Count the frequency of each character in the first string.
3. Traverse the second string and decrease the frequency.
4. If a character is missing or its count becomes negative, return `False`.
5. If all checks pass, return `True`.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
