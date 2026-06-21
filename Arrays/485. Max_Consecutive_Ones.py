# Intuition
Count consecutive 1s in the array and keep track of the maximum streak.

# Approach
1. Use a counter to track current consecutive 1s.
2. Use another variable to store the maximum count.
3. Traverse the array:
   - If the number is 1, increase the counter.
   - If the number is 0, reset the counter to 0.
4. Update the maximum count during traversal.
5. Return the maximum count.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count
