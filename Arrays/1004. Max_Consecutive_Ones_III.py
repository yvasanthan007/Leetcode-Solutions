# Intuition
Two strings are anagrams if they contain the same characters with the same frequencies. Instead of sorting every substring of `s`, we can use a sliding window of size `len(p)` and keep track of character frequencies. Whenever the frequency of the current window matches the frequency of `p`, we have found an anagram.

# Approach
1. If `len(s) < len(p)`, return an empty list because `p` cannot fit inside `s`.
2. Create two frequency arrays of size `26`:
   - `p_count` to store the frequencies of characters in `p`.
   - `window` to store the frequencies of the current window in `s`.
3. Fill `p_count` using the characters of `p`.
4. Traverse `s` using a sliding window:
   - Add the current character to `window`.
   - If the window size becomes greater than `len(p)`, remove the leftmost character.
   - Compare `window` and `p_count`. If they are equal, append the starting index of the window to the answer.
5. Return the list of starting indices.

# Complexity
- Time complexity:
  - `O(n)`, where `n = len(s)`. We traverse `s` once, and comparing two arrays of size `26` takes constant time.

- Space complexity:
  - `O(1)`, since both frequency arrays have a fixed size of `26`.

# Code
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        ans = []
        l = len(p)

        for r in range(len(s)):
            window[ord(s[r]) - ord('a')] += 1

            if r >= l:
                window[ord(s[r - l]) - ord('a')] -= 1

            if window == p_count:
                ans.append(r - l + 1)

        return ans
```
