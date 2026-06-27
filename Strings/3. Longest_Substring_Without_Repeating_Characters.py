# Intuition
We need to find the longest contiguous subarray that contains at most two distinct fruit types. Since we can only carry two types of fruits in our baskets, the problem becomes finding the longest subarray with at most two distinct elements.

A sliding window is perfect for this because we can expand the window while it contains at most two fruit types and shrink it whenever it contains more than two.

# Approach
1. Use two pointers, `l` and `r`, to represent the current window.
2. Maintain a hashmap `freq` to store the frequency of each fruit type in the current window.
3. Expand the window by moving `r` and add `fruits[r]` to `freq`.
4. If the window contains more than two distinct fruit types:
   - Shrink the window from the left.
   - Decrease the frequency of `fruits[l]`.
   - Remove the fruit type from the hashmap if its frequency becomes `0`.
   - Move `l` forward.
5. After every valid window, update the maximum length `ans`.
6. Return `ans`.

# Complexity
- Time complexity:
  - `O(n)`, where `n = len(fruits)`. Each element is added to and removed from the window at most once.

- Space complexity:
  - `O(1)`, since the hashmap stores at most three fruit types at any time (effectively constant space).

# Code
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        ans = 0
        freq = {}

        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1

            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
