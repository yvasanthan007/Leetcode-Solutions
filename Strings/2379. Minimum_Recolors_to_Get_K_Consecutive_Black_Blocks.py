# Intuition
To get `k` consecutive black blocks, we need to find a window of size `k` that contains the fewest white blocks. Every white block in that window must be recolored to black.

A sliding window of size `k` allows us to efficiently count the number of white blocks in each window and keep track of the minimum.

# Approach
1. Count the number of white blocks (`'W'`) in the first window of size `k`.
2. Initialize the answer with this count since these whites would need to be recolored.
3. Slide the window one position at a time:
   - Remove the leftmost character from the window. If it is `'W'`, decrement the white count.
   - Add the new character entering the window. If it is `'W'`, increment the white count.
   - Update the minimum number of recolors needed.
4. Return the minimum white count found.

# Complexity
- Time complexity:
  - `O(n)`, where `n = len(blocks)`. We traverse the string once.

- Space complexity:
  - `O(1)`, since only a few variables are used.

# Code
```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0

        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        ans = white
        left = 0

        for right in range(k, len(blocks)):
            if blocks[left] == 'W':
                white -= 1
            left += 1

            if blocks[right] == 'W':
                white += 1

            ans = min(ans, white)

        return ans
```
