# Intuition
We need to find the length of the longest substring containing exactly `k` distinct characters. A sliding window is suitable because we can expand the window to include new characters and shrink it whenever the number of distinct characters becomes greater than `k`.

We use a hashmap to store the frequency of characters in the current window and keep track of the maximum valid window length.

# Approach
1. Initialize two pointers, `left` and `right`, to represent the current window.
2. Use a hashmap `freq` to store the frequency of characters in the window.
3. Expand the window by moving `right`:
   - Add `s[right]` to `freq`.
4. If the number of distinct characters becomes greater than `k`:
   - Shrink the window from the left.
   - Decrease the frequency of `s[left]`.
   - Remove the character from the hashmap if its frequency becomes `0`.
5. Whenever the window contains exactly `k` distinct characters, update the answer with the current window size.
6. If no valid substring exists, return `-1`.

# Complexity
- Time complexity:
  - `O(n)`, where `n = len(s)`. Each character is added to and removed from the hashmap at most once.

- Space complexity:
  - `O(k)`, since the hashmap stores at most `k + 1` distinct characters.

# Code
```python
class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        freq = {}
        ans = -1

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if len(freq) == k:
                ans = max(ans, right - left + 1)

        return ans
```
