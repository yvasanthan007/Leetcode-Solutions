# Intuition
Since the array is sorted, we can use binary search to find the target efficiently by repeatedly dividing the search space in half.

# Approach
1. Set two pointers: low and high.
2. Find the middle element.
3. If it matches the target, return its index.
4. If the target is smaller, search the left half.
5. If the target is larger, search the right half.
6. If not found, return -1.

# Complexity
- Time complexity:
O(log n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1
