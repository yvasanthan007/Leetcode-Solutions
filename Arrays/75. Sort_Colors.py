# Intuition
Sort the array by repeatedly swapping adjacent elements if they are in the wrong order.

# Approach
1. Traverse the array multiple times.
2. Compare adjacent elements.
3. Swap them if they are not in sorted order.
4. After each pass, the largest element moves to its correct position.
5. Continue until the array is sorted.

# Complexity
- Time complexity:
O(n²)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
