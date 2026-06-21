# Intuition
We need the third distinct maximum number. So first remove duplicates and then sort the numbers in descending order.

# Approach
1. Convert the array into a set to remove duplicates.
2. Sort the unique numbers in descending order.
3. If there are at least 3 numbers, return the 3rd one.
4. Otherwise, return the maximum number.

# Complexity
- Time complexity:
O(n log n)

- Space complexity:
O(n)

# Code
```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)

        if len(nums) >= 3:
            return nums[2]

        return nums[0]
