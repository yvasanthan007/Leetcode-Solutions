# Intuition
Instead of calculating the average of every subarray of size `k`, we can compare the sum of each subarray with `k * threshold`. A sliding window of size `k` allows us to efficiently maintain the sum of the current subarray in constant time.

# Approach
1. Compute `target = k * threshold`.
2. Find the sum of the first window of size `k`.
3. If the sum is greater than or equal to `target`, increment the count.
4. Slide the window one element at a time:
   - Add the new element entering the window.
   - Remove the element leaving the window.
   - If the new window sum is at least `target`, increment the count.
5. Return the final count.

# Complexity
- Time complexity:
  - `O(n)`, where `n = len(arr)`. We traverse the array only once.

- Space complexity:
  - `O(1)`, since only a few variables are used.

# Code
```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window = 0

        for i in range(k):
            window += arr[i]

        c = 0
        if window >= target:
            c += 1

        for i in range(k, len(arr)):
            window += arr[i]
            window -= arr[i - k]

            if window >= target:
                c += 1

        return c
```
