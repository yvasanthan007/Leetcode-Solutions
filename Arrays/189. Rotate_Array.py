# Intuition
Rotate the array to the right by `k` positions by taking the last `k` elements and placing them at the beginning.

# Approach
1. Find the length of the array.
2. Compute `k % n` to handle large values of `k`.
3. Take the last `k` elements.
4. Append the remaining elements after them.
5. Update the original array in-place.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
