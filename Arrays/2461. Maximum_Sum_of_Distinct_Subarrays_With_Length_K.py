# Intuition
We need to find the maximum sum of a subarray of size `k` such that all elements in the subarray are distinct. Since we are dealing with contiguous subarrays of fixed size `k`, a sliding window approach is suitable.

To efficiently check whether all elements are distinct, we maintain a frequency hashmap. We also keep track of the current window's sum so that we don't have to recompute it every time the window moves.

# Approach
1. Use two pointers (`left` and `right`) to represent a sliding window.
2. Maintain:
   - `freq`: a hashmap storing the frequency of elements in the current window.
   - `window_sum`: the sum of elements in the current window.
3. Expand the window by moving `right`:
   - Add `nums[right]` to `window_sum`.
   - Increase its frequency in `freq`.
4. If the window size exceeds `k`:
   - Remove `nums[left]` from the window.
   - Decrease its frequency and delete it from the hashmap if its frequency becomes `0`.
   - Move `left` forward.
5. Whenever the window size becomes exactly `k`, check if `len(freq) == k`.
   - If true, all elements are distinct, so update the answer with the current `window_sum`.
6. Return the maximum sum obtained.

# Complexity
- Time complexity:
  - `O(n)` because each element is added to and removed from the window at most once.

- Space complexity:
  - `O(k)` for the frequency hashmap in the worst case when all elements in the window are distinct.

# Code
```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        window_sum = 0
        ans = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                window_sum -= nums[left]

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, window_sum)

        return ans
